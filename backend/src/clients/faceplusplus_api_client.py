import os

from tornado.httpclient import AsyncHTTPClient, HTTPRequest
from tornado.escape import json_decode, json_encode
from tornado.log import app_log

from urllib.parse import urlencode
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class FacePlusPlusApiClient:

    def __init__(self):
        self.client = AsyncHTTPClient()
        self.attributes = ['emotion']

    async def fetch_photo_faces(self, photo_uri):
        request = self._build_request(photo_uri)
        try:
            response = await self.client.fetch(request)
        except Exception as e:
            app_log.error("Face++Service: error while fetching faces for photo {photo}: {error}".format(
                photo=photo_uri,
                error=e
            ))
            raise e
        return json_decode(response.body)['faces']

    def _build_request(self, photo_uri):
        uri = self._build_photo_detect_uri(photo_uri)
        app_log.debug(
            "Face++Service: fetching faces from: {} for photo: {}".format(uri, photo_uri))
        api_key = os.getenv("FACEPLUSPLUS_API_KEY")
        api_secret = os.getenv("FACEPLUSPLUS_API_SECRET")
        if len(self.attributes) == 1:
            attributes = self.attributes[0]
        else:
            attributes = ','.join(attributes)

        body = (
            ('api_key', api_key),
            ('api_secret', api_secret),
            ('image_url', photo_uri),
            ('return_attributes', attributes)
        )

        return HTTPRequest(
            url=uri,
            method='POST',
            body=urlencode(body)
        )

    def _build_photo_detect_uri(self, photo_uri):
        api_uri = os.getenv("FACEPLUSPLUS_URI")
        api_method = os.getenv("FACEPLUSPLUS_DETECT_METHOD")
        return "{root}/{method}".format(root=api_uri, method=api_method)

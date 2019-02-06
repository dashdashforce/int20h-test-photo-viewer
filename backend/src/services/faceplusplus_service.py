# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import os
from urllib.parse import urlencode

from dotenv import find_dotenv, load_dotenv
from tornado.escape import json_decode, json_encode
from tornado.httpclient import AsyncHTTPClient, HTTPRequest
from tornado.log import app_log

load_dotenv(find_dotenv())


class FacePlusPlusService:

    def __init__(self):
        self.async_http_client = AsyncHTTPClient()
        self.emotions = [
            'sadness',
            'neutral',
            'disgust',
            'anger',
            'surprise',
            'fear',
            'happiness'
        ]
        self.attributes = ['emotion']

    def _build_photo_detect_uri(self, photo_uri):
        api_uri = os.getenv("FACEPLUSPLUS_URI")
        api_method = os.getenv("FACEPLUSPLUS_DETECT_METHOD")
        return "{root}/{method}".format(root=api_uri, method=api_method)

    def _build_request(self, photo_uri):
        uri = self._build_photo_detect_uri(photo_uri)
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

    def get_emotions(self):
        return self.emotions

    async def get_photo_face_data(self, photo_uri):
        request = self._build_request(photo_uri)
        app_log.debug("Face++ request: {}".format(request.body))
        response = await self.async_http_client.fetch(request)
        app_log.debug("Face++ response: {}".format(response.body))
        return json_decode(response.body)

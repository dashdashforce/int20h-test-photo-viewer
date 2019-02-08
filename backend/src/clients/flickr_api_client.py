
import os
import hashlib
import time
import hmac

from random import randint
from urllib.parse import urlencode, quote

from tornado.httpclient import AsyncHTTPClient, HTTPClient
from tornado.escape import json_decode, json_encode
from tornado.log import app_log


from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class FlickrApiClient:

    def __init__(self):
        self.client = AsyncHTTPClient()
        self.sync_client = HTTPClient()

    async def fetch_photos(self, page, limit):
        uri = self._build_album_request_uri(page, limit)
        app_log.debug('FlickrService: fetching photos from {}'.format(uri))
        try:
            response = await self.async_client.fetch(uri)
        except Exception as e:
            app_log.error(
                'FlickrService: error while fetching photos: {}'.format(e)
            )
            raise e
        return json_decode(response.body)['photoset']['photo']

    def fetch_photos_sync(self, page, limit):
        uri = self._build_album_request_uri(page, limit)
        return json_decode(self.sync_client.fetch(uri).body.decode("utf-8"))

    def _build_album_request_uri(self, page, limit):
        params = (
            ('method', os.getenv("FICKR_GET_BY_ALBUM_METHOD")),
            ('api_key', os.getenv("FLICKR_API_KEY")),
            ('photoset_id', os.getenv("FLICKR_ALBUM_ID")),
            ('user_id', os.getenv("FLICKR_USER_ID")),
            ('page', page),
            ('per_page', limit),
            ('format', 'json'),
            ('nojsoncallback', 1),
            ('extras', 'url_l,url_m,url_s')
        )

        return "{root}?{params}".format(
            root=os.getenv("FLICKR_URI"),
            params=urlencode(params)
        )

    """
        Deprecated
    """

    def _get_sig(self):
        consumer_key = os.getenv("FLICKR_API_KEY")
        request_url = os.getenv("FLICKR_URI")
        nonce = str(hashlib.md5(str(randint(0, 1000000)).encode())).encode()
        signature_method = "HMAC-SHA1"
        time_stamp = time.time()
        version = "1.0"

        sig_base = "GET&" + quote(request_url) + "&"
        sig_base += quote("oauth_consumer_key=" + quote(consumer_key))
        sig_base += quote("&oauth_nonce=" + quote(nonce))
        sig_base += quote("&oauth_signature_method=" + quote(signature_method))
        sig_base += quote("&oauth_timestamp=" + str(time_stamp))
        sig_base += quote("&oauth_version=" + version)

        sig_key = consumer_key + "&"
        print(hmac.new(sig_key.encode(), sig_base.encode(), hashlib.sha1).hexdigest())
        return hmac.new(sig_key.encode(), sig_base.encode(), hashlib.sha1).hexdigest()

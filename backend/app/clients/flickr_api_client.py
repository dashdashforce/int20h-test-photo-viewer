
import hashlib
import hmac
import os
import time
from random import randint
from urllib.parse import quote, urlencode

from dotenv import find_dotenv, load_dotenv
from tornado.escape import json_decode, json_encode
from tornado.httpclient import AsyncHTTPClient, HTTPClient
from tornado.log import app_log

load_dotenv(find_dotenv())


class FlickrApiClient:

    default_tag = '#int20h'

    def __init__(self):
        self.client = AsyncHTTPClient()
        self.sync_client = HTTPClient()

    async def fetch_album_photos(self, page, limit):
        uri = self._build_album_request_uri(page, limit)
        app_log.debug('FlickrService: fetching photos from {}'.format(uri))
        try:
            response = await self.client.fetch(uri)
        except Exception as e:
            app_log.error(
                'FlickrService: error while fetching photos: {}'.format(e)
            )
            raise e
        return json_decode(response.body)['photoset']

    def fetch_album_photos_sync(self, page, limit):
        uri = self._build_album_request_uri(page, limit)
        return json_decode(self.sync_client.fetch(uri).body.decode("utf-8"))

    def _build_album_request_uri(self, page, limit):
        extras = [
            'url_l', 'url_m', 'url_s', 'tags'
        ]
        params = (
            ('method', os.getenv("FICKR_GET_BY_ALBUM_METHOD")),
            ('api_key', os.getenv("FLICKR_API_KEY")),
            ('photoset_id', os.getenv("FLICKR_ALBUM_ID")),
            ('user_id', os.getenv("FLICKR_USER_ID")),
            ('page', page),
            ('per_page', limit),
            ('format', 'json'),
            ('nojsoncallback', 1),
            ('extras', ','.join(extras))
        )

        return "{root}?{params}".format(
            root=os.getenv("FLICKR_URI"),
            params=urlencode(params)
        )

    async def fetch_photos_by_tag(self, page, limit):
        uri = self._build_search_request_uri(page, limit)
        try:
            response = await self.client.fetch(uri)
        except Exception as e:
            app_log.error(
                'FlickrService: error while fetching photos by tag: {}'
                .format(e)
            )
            raise e
        return json_decode(response.body)['photos']

    def _build_search_request_uri(self, page, limit):
        extras = [
            'url_l', 'url_m', 'url_s', 'tags'
        ]
        params = (
            ('method', 'flickr.photos.search'),
            ('api_key', os.getenv("FLICKR_API_KEY")),
            ('tags', self.default_tag),
            ('page', page),
            ('format', 'json'),
            ('nojsoncallback', 1),
            ('per_page', limit),
            ('extras', ','.join(extras))

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

from tornado.httpclient import AsyncHTTPClient
from tornado.httpclient import HTTPClient
from tornado.escape import json_decode, json_encode
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
import os
import time
import hashlib
from urllib.parse import quote
from random import randint
from base64 import encodestring
import hmac



from ..repository.photos_repository import PhotosRepository

class FlickApiService():
    
    def __init__(self):
        self.repository = PhotosRepository()
        self.async_client = AsyncHTTPClient()
        self.client = HTTPClient()

    def fetch_sync(self, page):
        print(self.get_album_request_uri(page))
        return json_decode(self.client.fetch(self.get_album_request_uri(page)).body.decode("utf-8"))

    def get_album_request_uri(self, page):
        return os.getenv("FLICKR_URI") + "?method=" + os.getenv("FICKR_GET_BY_ALBUM_METHOD") + "&api_key=" + os.getenv("FLICKR_API_KEY") + "&photoset_id=" + os.getenv("FLICKR_ALBUM_ID") + "&user_id=" + os.getenv("FLICKR_USER_ID") + "&page=" + str(page) +"&per_page=100&format=json&nojsoncallback=1&api_sig=" + self.get_sig()

    def save_photos(self, photos):
        self.repository.batch_insert(self.transform_photos(photos))

    def transform_photos(self, photos):
        result = []
        for photo in photos:
            photo._id = photo.id
            result.append(photo)
        return result

    def get_sig(self):
        consumer_key = os.getenv("FLICKR_API_KEY")
        requesr_url = os.getenv("FLICKR_URI")
        nonce = str(hashlib.md5(str(randint(0, 1000000)).encode())).encode()
        signature_method = "HMAC-SHA1"
        time_stamp = time.time()
        version = "1.0"

        sig_base = "GET&" + quote(requesr_url) + "&"
        sig_base += quote("oauth_consumer_key=" + quote(consumer_key))
        sig_base += quote("&oauth_nonce=" + quote(nonce))
        sig_base += quote("&oauth_signature_method=" + quote(signature_method))
        sig_base += quote("&oauth_timestamp=" + str(time_stamp))
        sig_base += quote("&oauth_version=" + version)

        sig_key = consumer_key + "&"
        print(hmac.new(sig_key.encode(), sig_base.encode(), hashlib.sha1).hexdigest())
        return hmac.new(sig_key.encode(), sig_base.encode(), hashlib.sha1).hexdigest()
        

    async def fetch_async(self, page):
        await self.async_client.fetch(self.get_album_request_uri(page), lambda response: self.save_photos(json_decode(response).photoset.photo))
        

    
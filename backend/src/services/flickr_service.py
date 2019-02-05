from tornado.httpclient import AsyncHTTPClient
from tornado.httpclient import HTTPClient
from tornado.escape import json_decode, json_encode
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
import os

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
        return os.getenv("FLICKR_URI") + "?method=" + os.getenv("FICKR_GET_BY_ALBUM_METHOD") + "&api_key=" + os.getenv("FLICKR_API_KEY") + "&photoset_id=" + os.getenv("FLICKR_ALBUM_ID") + "&user_id=" + os.getenv("FLICKR_USER_ID") + "&page=" + str(page) +"&per_page=100&format=json&nojsoncallback=1&api_sig=0ee6b2cd54e9e7465438dbcf0ff6b158"

    def save_photos(self, photos):
        self.repository.batch_insert(self.transform_photos(photos))

    def transform_photos(self, photos):
        result = []
        for photo in photos:
            photo._id = photo.id
            result.append(photo)
        return result

    async def fetch_async(self, page):
        await self.async_client.fetch(self.get_album_request_uri(page), lambda response: self.save_photos(json_decode(response).photoset.photo))
        

    

from ..clients import FlickrApiClient
from ..repository.photos_repository import PhotosRepository


class PhotoService():

    def __init__(self):
        self.repository = PhotosRepository()
        self.client = FlickrApiClient()

    async def get_photos(self, page, limit):
        cached_photos = await self.repository.get_photos()
        if not cached_photos:
            photos = await self.client.fetch_album_photos(page, limit)
            await self.repository.save_photos(photos)
        else:
            photos = cached_photos

        return photos


from tornado.web import HTTPError

from ..clients import FlickrApiClient
from ..repository.photos_repository import PhotosRepository


class PhotoService():

    def __init__(self):
        self.repository = PhotosRepository()
        self.client = FlickrApiClient()

    """
        after_photo - id of photo. After this photo page starts
        first - count of photo
    """
    async def get_photos(self, first=20, after_photo=None):
        return await self.repository.get_photos(first, after_photo)

    async def get_photo(self, id):
        photo = await self.repository.get_photo(id)
        if photo:
            return photo
        raise HTTPError(
            status_code=404,
            reason="Photo with id {} not found".format(id)
        )

    async def get_filtered_photos(self, filters, first, after, map_func):
        filtering_page = first
        photos = list(map(map_func, await self.get_photos(filtering_page, after)))
        filtered_photos = await self._get_filtered_photos(photos, filters)
        while len(filtered_photos) < first:
            filtering_page = first * 2
            photos = list(map(map_func, await self.get_photos(filtering_page, photos[-1].id)))
            if len(photos) == 0:
                break
            filtered_photos += await self._get_filtered_photos(photos, filters)

        return filtered_photos[:first]

    async def _get_filtered_photos(self, photos, filters):
        filtered_photos = []
        for photo in photos:
            is_confirm = await self._is_photo_confirm_filter(photo, filters)
            if is_confirm:
                filtered_photos.append(photo)
        return filtered_photos

    async def _is_photo_confirm_filter(self, photo, filters):
        faces = await photo.resolve_faces(None)
        for face in faces:
            top_emotion = face.resolve_top_emotion(None)
            if top_emotion in filters:
                return True
        return False

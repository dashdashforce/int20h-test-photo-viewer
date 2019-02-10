
import os
from urllib.parse import urlencode

from tornado.log import app_log

from ..clients import FacePlusPlusApiClient
from ..repository import EmotionsRepository, FacesRepository


class FaceService:

    def __init__(self):
        self.faces_repository = FacesRepository()
        self.emotions_repository = EmotionsRepository
        self.client = FacePlusPlusApiClient()

    def get_emotions(self):
        return self.emotions_repository.get_emotions()

    async def get_photo_faces(self, photo_uri, photo_id):
        cached_faces = await self.faces_repository.get_faces(photo_id)

        if cached_faces is None:
            faces = await self.client.fetch_photo_faces(photo_uri)
            await self.faces_repository.save_faces(faces, photo_id)
        else:
            faces = cached_faces

        return faces

# -*- coding: utf-8 -*-

import os

from motor.motor_tornado import MotorClient
from tornado.log import app_log


class FacesRepository:

    def __init__(self):
        db_url = os.getenv("MONGODB_URL")
        db_name = os.getenv("MONGODB_DB")
        self.collection = MotorClient(db_url)[db_name].faces

    async def save_faces(self, faces, photo_id):
        document = {
            'faces': faces,
            'photo_id': photo_id
        }
        app_log.debug(
            'FacesRepository: saving faces in cache for photo {}'.format(photo_id))
        result = await self.collection.insert_one(document)

    async def get_faces(self, photo_id):
        result = await self.collection.find_one({'photo_id': photo_id})
        if result:
            faces = result['faces']
            app_log.debug(
                'FacesRepository: get faces from cache for photo {}, faces: {}'.format(photo_id, faces))
            return faces
        else:
            return None

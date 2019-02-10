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
            '_id': photo_id,
            'faces': faces
        }
        app_log.debug(
            'FacesRepository: saving faces in cache for photo {}'.format(photo_id))
        try:
            result = await self.collection.insert_one(document)
        except Exception as e:
            app_log.warn(
                'Cannot save faces for photo {}: {}'.format(photo_id, faces))

    async def get_faces(self, photo_id):
        result = await self.collection.find_one({'_id': photo_id})
        if result:
            faces = result['faces']
            app_log.debug(
                'FacesRepository: get faces from cache for photo {}, faces: {}'.format(photo_id, faces))
            return faces
        else:
            return None

# -*- coding: utf-8 -*-

import motor.motor_tornado
import os
import pprint
#from __future__ import absolute_import, division, print_function

"""
    TODO Integrate repository with db
"""
class FacesRepository:

    def __init__(self):
        self.collection = ((motor.motor_tornado.MotorClient(os.getenv("MONGODB_URL")))[
                        os.getenv("MONGODB_DB")]).faces

    async def save_faces(self, faces, photo_uri):
        document = {
            'faces': faces,
            'photo_uri': photo_uri
        }
        result = await self.collection.insert_one(document)

    async def get_faces(self, photo_uri):
        result = await self.collection.find_one({'photo_uri': photo_uri})
        if result:
            return result.faces
        else:
            return None

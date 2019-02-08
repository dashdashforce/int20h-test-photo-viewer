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
        print('begin')
        self.collection = ((motor.motor_tornado.MotorClient(os.getenv("MONGODB_URL")))[
                        os.getenv("MONGODB_DB")]).faces
        self.faces_cache = {}

    async def save_faces(self, faces, photo_uri):
        self.faces_cache[photo_uri] = faces

    async def get_faces(self, photo_uri):
        if photo_uri in self.faces_cache:
            return self.faces_cache[photo_uri]
        else:
            return None
    
    async def test(self):
        document = await self.collection.find_one({'_id': '//'})
        pprint.pprint(document)

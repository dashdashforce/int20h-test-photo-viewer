# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

"""
    TODO Integrate repository with db
"""
class FacesRepository:

    def __init__(self):
        self.faces_cache = {}

    async def save_faces(self, faces, photo_uri):
        self.faces_cache[photo_uri] = faces

    async def get_faces(self, photo_uri):
        if photo_uri in self.faces_cache:
            return self.faces_cache[photo_uri]
        else:
            return None

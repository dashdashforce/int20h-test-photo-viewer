# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from .face_service import FaceService
from .photo_service import PhotoService


class ServiceLocator:

    def __init__(self):
        self.face_service = FaceService()
        self.photo_service = PhotoService()

# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from .faceplusplus_service import FacePlusPlusService


class ServiceLocator:

    def __init__(self):
        self.faceplusplus_service = FacePlusPlusService()
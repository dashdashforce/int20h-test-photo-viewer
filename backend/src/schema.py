# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from collections import OrderedDict

import graphene
from tornado import gen

from .services import service_locator
from tornado.log import app_log
from pprint import pprint


class Emotion(graphene.ObjectType):
    title = graphene.String()


class FaceEmotion(graphene.ObjectType):
    title = graphene.String()
    factor = graphene.Float()


class FaceRectangle(graphene.ObjectType):
    height = graphene.Int()
    width = graphene.Int()
    top = graphene.Int()
    left = graphene.Int()


class Face(graphene.ObjectType):
    face_rectangle = graphene.Field(FaceRectangle)
    emotion = graphene.List(FaceEmotion)

    @classmethod
    def map(cls, face_dict):
        face_rectangle_dict = face_dict['face_rectangle']
        if 'attributes' in face_dict:
            emotion_factors = face_dict['attributes']['emotion']
        else:
            emotion_factors = {}

        face_rectangle = FaceRectangle(
            face_rectangle_dict['height'],
            face_rectangle_dict['width'],
            face_rectangle_dict['top'],
            face_rectangle_dict['left']
        )

        face_emotions = [
            FaceEmotion(emotion, factor) for emotion, factor in emotion_factors.items()
        ]

        return Face(face_rectangle, face_emotions)


class PhotoSize(graphene.ObjectType):
    width = graphene.Int()
    height = graphene.Int()
    url = graphene.String()


class PhotoSizes(graphene.ObjectType):
    small = graphene.Field(PhotoSize)
    medium = graphene.Field(PhotoSize)
    large = graphene.Field(PhotoSize)


class Photo(graphene.ObjectType):
    id = graphene.ID()
    title = graphene.String()
    sizes = graphene.Field(PhotoSizes)

    faces = graphene.List(Face)

    async def resolve_faces(self, info):
        faceplusplus_service = service_locator.faceplusplus_service
        faces = await faceplusplus_service.get_photo_faces(self.sizes.large.url, self.id)
        return map(Face.map, faces)

    @classmethod
    def map(cls, photo_dict):
        id = photo_dict['id']
        title = photo_dict['title']
        large_size = PhotoSize(
            photo_dict['width_l'],
            photo_dict['height_l'],
            photo_dict['url_l']
        )
        medium_size = PhotoSize(
            photo_dict['width_m'],
            photo_dict['height_m'],
            photo_dict['url_m']
        )

        small_size = PhotoSize(
            photo_dict['width_s'],
            photo_dict['height_s'],
            photo_dict['url_s']
        )
        return Photo(
            id,
            title,
            PhotoSizes(small_size, medium_size, large_size)
        )


class Query(graphene.ObjectType):
    photos = graphene.List(Photo,
                           filters=graphene.List(
                               graphene.String, default_value=[]),
                           limit=graphene.Int(default_value=20),
                           page=graphene.Int(default_value=1))

    emotions = graphene.List(Emotion, limit=graphene.Int(default_value=20))

    """
        TODO Implement photo filtering by emotions
        `filters` param is list of emotion titles
    """
    async def resolve_photos(self, info, filters, limit, page):
        flickr_service = service_locator.flickr_service
        photos = await flickr_service.get_photos(page, limit)
        return map(Photo.map, photos)

    def resolve_emotions(self, info, limit):
        faceplusplus_service = service_locator.faceplusplus_service
        emotions = faceplusplus_service.get_emotions()[:limit]
        return map(lambda title: Emotion(title), emotions)


schema = graphene.Schema(query=Query)

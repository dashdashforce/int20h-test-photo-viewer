# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from collections import OrderedDict

import graphene
from tornado import gen

from .services import service_locator


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


class Photo(graphene.ObjectType):
    id = graphene.ID()
    title = graphene.String()
    url = graphene.String()
    width = graphene.Int()
    height = graphene.Int()

    faces = graphene.List(Face)

    def map_face(self, face):
        face_rectangle_dict = face['face_rectangle']
        emotion_factors = face['attributes']['emotion']

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

    async def resolve_faces(self, info):
        faceplusplus_service = service_locator.faceplusplus_service
        faces_data = await faceplusplus_service.get_photo_face_data(self.url)
        return map(self.map_face, faces_data['faces'])


class Query(graphene.ObjectType):
    photos = graphene.List(Photo,
                           filters=graphene.List(
                               graphene.String, default_value=[]),
                           limit=graphene.Int(default_value=20))

    emotions = graphene.List(Emotion, limit=graphene.Int(default_value=20))

    def resolve_photos(self, info, filters, limit):
        return [
            Photo(
                '1',
                'Sadness photo',
                'https://images.pexels.com/photos/568021/pexels-photo-568021.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260',
                1260,
                750
            ),
        ]

    def resolve_emotions(self, info, limit):
        faceplusplus_service = service_locator.faceplusplus_service
        emotions = faceplusplus_service.get_emotions()[:limit]
        return map(lambda title: Emotion(title), emotions)


schema = graphene.Schema(query=Query)

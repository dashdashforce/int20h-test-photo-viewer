
from collections import OrderedDict
from datetime import datetime

import graphene
from tornado import gen
from tornado.log import app_log

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
    top_emotion = graphene.String()

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

    def resolve_top_emotion(self, info):
        max_factor = 0
        top_emotion = ''
        for emotion_part in self.emotion:
            if emotion_part.factor > max_factor:
                max_factor = emotion_part.factor
                top_emotion = emotion_part.title
        return top_emotion


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
    upload_date = graphene.String()

    faces = graphene.List(Face)

    async def resolve_faces(self, info):
        face_service = service_locator.face_service
        faces = await face_service.get_photo_faces(self.sizes.large.url, self.id)
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
        upload_timestamp = int(photo_dict['dateupload'])
        upload_date = datetime.fromtimestamp(upload_timestamp).isoformat()

        return Photo(
            id,
            title,
            PhotoSizes(small_size, medium_size, large_size),
            upload_date
        )


class Query(graphene.ObjectType):
    photos = graphene.List(Photo,
                           filters=graphene.List(
                               graphene.String, default_value=[]),
                           first=graphene.Int(default_value=20),
                           after=graphene.String(default_value=""))

    emotions = graphene.List(Emotion, limit=graphene.Int(default_value=20))

    """
        TODO Implement photo filtering by emotions
        `filters` param is list of emotion titles
    """
    async def resolve_photos(self, info, filters, first, after):
        if len(after) == 0:
            after = None
        photo_service = service_locator.photo_service

        if len(filters) != 0:
            return photo_service.get_filtered_photos(filters, first, after, Photo.map)
        else:
            photos = await photo_service.get_photos(first, after)
            photos = map(Photo.map, photos)
            return photos

    def resolve_emotions(self, info, limit):
        face_service = service_locator.face_service
        emotions = face_service.get_emotions()[:limit]
        return map(lambda title: Emotion(title), emotions)


schema = graphene.Schema(query=Query)

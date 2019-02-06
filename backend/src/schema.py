# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from collections import OrderedDict

import graphene
from .services import service_locator


class Emotion(graphene.ObjectType):
    title = graphene.String()


class Photo(graphene.ObjectType):
    id = graphene.ID()
    title = graphene.String()
    url = graphene.String()
    width = graphene.Int()
    height = graphene.Int()

    emotions = graphene.List(Emotion)

    def resolve_emotions(self, info):
        return []


class Query(graphene.ObjectType):
    photos = graphene.List(Photo,
                           filters=graphene.List(
                               graphene.String, default_value=[]),
                           limit=graphene.Int(default_value=20))

    emotions = graphene.List(Emotion, limit=graphene.Int(default_value=20))

    def resolve_photos(self, info, filters, limit):
        return []

    def resolve_emotions(self, info, limit):
        faceplusplus_service = service_locator.faceplusplus_service
        emotions = faceplusplus_service.get_emotions()[:limit]
        return map(lambda title: Emotion(title), emotions)


schema = graphene.Schema(query=Query)

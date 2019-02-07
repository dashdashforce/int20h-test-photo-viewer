# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from graphene_tornado.tornado_graphql_handler import TornadoGraphQLHandler
from tornado.web import Application

from .graphql import GraphQLHandler
from .schema import schema


class MainApplicationHandler(GraphQLHandler):

    def initialize(self, opts):
        super(MainApplicationHandler, self).initialize()
        self.opts = opts
        self._schema = schema

    @property
    def schema(self):
        return self._schema


class PhotoViewerApiApplication(Application):

    def __init__(self, settings):
        self.opts = dict(settings)

        handlers = [
            (r'/graphql', TornadoGraphQLHandler, dict(
                graphiql=True, schema=schema
            )),
        ]

        super(PhotoViewerApiApplication, self).__init__(handlers, **settings)

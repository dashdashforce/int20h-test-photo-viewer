# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

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
            (r'/graphql', MainApplicationHandler, dict(opts=self.opts)),
        ]

        super(PhotoViewerApiApplication, self).__init__(handlers, **settings)
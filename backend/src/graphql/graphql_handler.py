# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from tornado.web import RequestHandler
from tornado.escape import json_decode, json_encode


class GraphQLHandler(RequestHandler):

    def post(self):
        self.write(json_encode({
            "message": "Hello world"
        }))

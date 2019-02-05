# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from tornado.escape import json_decode, json_encode
from tornado.log import app_log
from tornado.web import RequestHandler

from .error_handler import GraphQLExecutionError, graphql_error_handler


class GraphQLHandler(RequestHandler):

    @graphql_error_handler
    def post(self):
        return self.handle_qraphql()

    def handle_qraphql(self):
        result = self.execute_graphql()
        app_log.debug('GraphQL result data: %s errors: %s invalid %s',
                      result.data, result.errors, result.invalid)

        if result and result.invalid:
            exception = GraphQLExecutionError(errors=result.errors)
            app_log.warn('GraphQL Error: %s', exception)
            raise exception

        response = {'data': result.data}
        self.write(json_encode(response))

    def execute_graphql(self):
        graphql_request = self.graphql_request
        app_log.debug('graphql request: %s', graphql_request)
        return self.schema.execute(
            graphql_request.get('query'),
            variable_values=graphql_request.get('variables'),
            operation_name=graphql_request.get('operationName'),
            context_value=graphql_request.get('context'),
            middleware=self.middleware
        )

    @property
    def graphql_request(self):
        return json_decode(self.request.body)

    @property
    def schema(self):
        raise NotImplementedError('graphql schema must be provided')

    @property
    def middleware(self):
        return []

# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import sys
import traceback
from functools import wraps

from graphql.error import GraphQLError
from graphql.error import format_error as format_graphql_error
from tornado.escape import json_encode
from tornado.log import app_log
from tornado.web import HTTPError


def error_status(exception):
    if isinstance(exception, HTTPError):
        return exception.status_code
    elif isinstance(exception, (GraphQLExecutionError, GraphQLError)):
        return 400
    else:
        return 500


def error_format(exception):
    if isinstance(exception, GraphQLExecutionError):
        return [{'message': e} for e in exception.errors]
    elif isinstance(exception, GraphQLError):
        return [format_graphql_error(exception)]
    elif isinstance(exception, HTTPError):
        return [{'message': exception.log_message,
                 'reason': exception.reason}]
    else:
        return [{'message': 'Unknown server error'}]


def graphql_error_handler(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            result = func(self, *args, **kwargs)
        except Exception as exception:
            if not isinstance(exception, (HTTPError, GraphQLExecutionError, GraphQLError)):
                tb = ''.join(traceback.format_exception(*sys.exc_info()))
                app_log.error('Error: {0} {1}'.format(exception, tb))
            self.set_status(error_status(exception))
            error_json = json_encode({'errors': error_format(exception)})
            app_log.debug('error_json: %s', error_json)
            self.write(error_json)
        else:
            return result

    return wrapper


class GraphQLExecutionError(Exception):
    def __init__(self, status_code=400, errors=None):
        self.status_code = status_code
        if errors is None:
            self.errors = []
        else:
            self.errors = [str(e) for e in errors]
        self.message = '\n'.join(self.errors)

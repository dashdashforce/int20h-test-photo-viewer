# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import sys

import tornado.ioloop
import tornado.web
from tornado.httpserver import HTTPServer
from traitlets import Bool, Dict, Integer, Unicode
from traitlets.config.application import Application, catch_config_error

from .version import __version__
from .web_app import PhotoViewerApiApplication


class PhotoViewerApplication(Application):
    name = '--force photo viewer app'
    version = __version__

    ip = Unicode(
        '', config=True,
        help='The IP address the server will listen on.'
    )

    port = Integer(
        8888, config=True,
        help='The port the server will listen on.'
    )

    application_settings = Dict(
        config=True,
        help='tornado.web.Application settings.'
    )

    def init_webapp(self):
        self.web_app = PhotoViewerApiApplication(self.application_settings)
        self.http_server = HTTPServer(self.web_app)
        self.http_server.listen(self.port, self.ip)

    @catch_config_error
    def initialize(self, argv=None):
        if argv is None:
            argv = sys.argv[1:]
        if argv:
            if argv[0] in self.subcommands.keys():
                self.subcommand = self.name + '-' + argv[0]
                self.argv = argv
                return

        super(PhotoViewerApplication, self).initialize(argv)

        self.init_webapp()

    def start(self):
        super(PhotoViewerApplication, self).start()
        self.io_loop = tornado.ioloop.IOLoop.current()
        try:
            self.io_loop.start()
        except KeyboardInterrupt:
            self.log.info('PhotoViewerApplication interrupted...')

    def stop(self):
        def _stop():
            self.http_server.stop()
            self.io_loop.stop()
        self.io_loop.add_callback(_stop)


main = launch_new_instance = PhotoViewerApplication.launch_instance

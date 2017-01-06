#!/usr/bin/env python
import logging
import os
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpserver
import tornado.autoreload

from tornado.options import options

from handlers import MainHandler, DataSocketHandler
from settings import settings, template_dir, static_dir
from utils import read_csv


class DataExplorer(object):

    def __init__(self, *args, **kwargs):
        self.data = kwargs.get('data', None)
        self.config = kwargs.get('config', None)

    def read_csv(self, filename, **kwargs):
        self.data = read_csv(filename, **kwargs)

    def start(self):
        tornado.options.parse_command_line()
        handlers = [
            (r"/", MainHandler),
            (r'/ws', DataSocketHandler,
                dict(data=self.data, config=self.config)
             )
        ]
        app = tornado.web.Application(handlers, **settings)
        http_server = tornado.httpserver.HTTPServer(app)
        logging.info("Listening on port %s" % options.port)
        http_server.listen(options.port)
        tornado.autoreload.start()
        tornado.autoreload.watch(os.path.join(template_dir, 'index.html'))
        tornado.autoreload.watch(os.path.join(static_dir, 'js/app.js'))
        tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    dte = DataExplorer()
    dte.read_csv('tweets.csv')
    dte.start()

#!/usr/bin/env python
import logging
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpserver
import tornado.autoreload

from tornado.options import options

from handlers import MainHandler, DataSocketHandler
from settings import settings


class DataExplorer(object):

    def __init__(self, *args, **kwargs):
        self.data = kwargs.get('data', None)
        self.config = kwargs.get('config', None)

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
        tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    DataExplorer().start()

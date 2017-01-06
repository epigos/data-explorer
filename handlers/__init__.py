from tornado import websocket, web, gen, escape

from .views import BaseView


class MainHandler(web.RequestHandler):

    @web.asynchronous
    def get(self):
        self.render("index.html")


class DataSocketHandler(websocket.WebSocketHandler):

    def initialize(self, data, config):
        self.view = BaseView(data, config)

    def check_origin(self, origin):
        return True

    def open(self):
        print("WebSocket opened")

    def on_close(self):
        print("WebSocket closed")

    def on_message(self, data):
        data = escape.json_decode(data)
        if 'summary' in data.get('message', ''):
            self.process_summary_data()
        if 'table' in data.get('message', ''):
            self.process_table_data()

    def send(self, data):
        self.write_message(data)

    @gen.coroutine
    def process_summary_data(self):
        yield self.view.get_data_summary(self.send)
        yield self.view.describe_columns(self.send)
        yield self.view.plot_columns(self.send)

    @gen.coroutine
    def process_table_data(self):
        pass

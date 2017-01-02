from tornado import websocket, web, escape


class MainHandler(web.RequestHandler):

    @web.asynchronous
    def get(self):
        self.render("index.html")


class DataSocketHandler(websocket.WebSocketHandler):

    def initialize(self, data, config):
        self.data = data
        self.config = config

    def check_origin(self, origin):
        return True

    def open(self):
        print("WebSocket opened")
        self.send({'msg': 'WebSocket opened'})

    def on_close(self):
        print("WebSocket closed")

    def on_message(self, message):
        data = escape.json_decode(message)
        print(data)

    def send(self, data):
        self.write_message(data)

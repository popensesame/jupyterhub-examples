
import tornado.web

class TestPageHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("Success!")





import tornado.ioloop as ioloop
import tornado.web as web

from jupyterhub.services.auth import HubAuth, HubAuthenticated

api_url = 'http://127.0.0.1:8000/hub/api'
# Keep it secret, keep it safe
token = '2f9d88896b7cf390a4c3f1d0e8a813e4de563a87d33bd3fd3ad09a25d513295a'

auth = HubAuth(
    api_url=api_url,
    api_token=token,
    cache_max_age=60,
    login_url='http://127.0.0.1:8000/hub/login',
)


class MainHandler(HubAuthenticated, web.RequestHandler):

    def initialize(self, hub_auth):
        self.hub_auth = hub_auth

    @web.authenticated
    def get(self):
        self.write("Success!")


def make_app():
    return web.Application([
        (r"/", MainHandler, dict(hub_auth=auth)),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    ioloop.IOLoop.current().start()


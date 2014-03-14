#-*- coding : utf-8 -*-
from tornado import ioloop,web
import tornado
import os

import handlers

from config import settings

class Application(tornado.web.Application):
    def __init__(self,route,settings):
        web.Application.__init__(self, route, **settings)
        # i18n 
        tornado.locale.load_gettext_translations(self.settings['i18n_path'], "tomatodo")


route = list([
    (r"/",web.RedirectHandler, dict(url = "/index.html") ),
    (r"/(index\.html)",web.StaticFileHandler,dict(path = settings['project_path']))
])


def main():
    app = Application(route,settings)
    app.listen(8888)
    try:
        ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        print("exit")
        ioloop.IOLoop.instance().stop()

if __name__ == "__main__":
    main()
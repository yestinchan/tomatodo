#-*- coding : utf-8 -*-
import tornado.ioloop
import tornado.web
import os

import handlers

from config import settings

class Application(tornado.web.Application):
    def __init__(self,route,settings):
        tornado.web.Application.__init__(self, route, **settings)
        # i18n 
        tornado.locale.load_gettext_translations(self.settings['i18n_path'], "tomatodo")


route = list([
    (r"/",handlers.MainHandler)
])


def main():
    app = Application(route,settings)
    app.listen(8888)
    try:
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        print("exit")
        tornado.ioloop.IOLoop.instance().stop()

if __name__ == "__main__":
    main()
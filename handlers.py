#-*- coding : utf-8 -*-

import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        return self.render("index.html")
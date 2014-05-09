__author__ = 'ReS4'

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        # self.write("hello reza")
        self.render('base/index.html')

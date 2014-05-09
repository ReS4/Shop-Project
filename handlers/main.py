__author__ = 'ReS4'

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from pymongo import MongoClient

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        # self.write("hello reza")
        self.render('base/index.html')

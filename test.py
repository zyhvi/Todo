#!/usr/bin/env python
#coding:utf-8

import tornado.web
import tornado.ioloop

import tornado.httpserver
import torndb
import os.path
from config.options import *
from controllers import controller




class Test(tornado.web.Application):
	def __init__(self):
		Handlers = [
                  (r'/', controller.IndexHandler),
                  (r'/todo/new', controller.NewHandler),
                  (r'/todo/(\d+)/delete', controller.DelHandler),
                  (r'/todo/(\d+)/finish', controller.FinishedHandler),
                  (r'/todo/(\d+)/edit', controller.EditHandler),
		]

		settings = dict(
	    	debug = True,
	    	blog_title = 'Todo',
	    	template_path = 'templates',
	    	static_path= "static",
	    	#template_path=os.path.join(os.path.dirname(__file__), "templates"),
            #static_path=os.path.join(os.path.dirname(__file__), "static"),
		    )

		tornado.web.Application.__init__(self, Handlers, **settings)

	


if __name__ == '__main__':
	http_server = tornado.httpserver.HTTPServer(Test())
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()

#!/usr/bin/env python
#coding: utf-8

import tornado.web
from config.options import *

def get_by_id(id):
	s = db.query('SELECT * FROM todo WHERE id = %s',(id))
	if not s:
		return False
	return s[0]

class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		todos = db.query('SELECT * FROM todo ORDER by finished ASC,id DESC')
		self.render('index.html', todos = todos)

class NewHandler(tornado.web.RequestHandler):
	def post(self):
		title = self.get_argument('title', None)
		if not title:
			raise tornado.web.HTTPError(404, 'test')
		db.execute('INSERT INTO todo (title, post_date) VALUES (%s, UTC_TIMESTAMP())',(title))
		self.redirect('/')
class DelHandler(tornado.web.RequestHandler):
	
	def get(self, id):
		todo = get_by_id(id)
		if not todo:
			raise tornado.web.HTTPError(404)
		db.execute('DELETE FROM todo WHERE id = %s',(id))
		self.redirect('/')
class FinishedHandler(tornado.web.RequestHandler):
	def get(self, id):
		todo = get_by_id(id)
		if not todo:
			raise tornado.web.HTTPError(404)
		status = self.get_argument('status', 'yes')
		if status == 'yes':
			finished = 1
		elif status =='no':
			finished = 0
		else:
			raise tornado.web.HTTPError(404)

		db.execute("UPDATE todo SET finished = %s WHERE id = %s",finished, id)
		self.redirect('/')
class EditHandler(tornado.web.RequestHandler):
	def get(self, id):
		todo = get_by_id(id)
		if not todo:
			self.render('error.html') 
		todos = db.query('SELECT * FROM todo ORDER by finished ASC,id DESC')
		self.render('edit.html', todos = todos, edit=todo)
	def post(self, id):
		todo = get_by_id(id)
		if not todo:
			self.render('error.html')
		title = self.get_argument('title')
		if not title:
			self.render('error.html')
		db.execute('UPDATE todo SET title = %s WHERE id = %s',title, id)
		self.redirect('/')

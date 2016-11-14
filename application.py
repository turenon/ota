#!/usr/bin/env python
#coding:utf-8
from url import url
import tornado.web
import os
from handler.base import *


#类似这样用法可以直接在html里调用#
class userModule(tornado.web.UIModule):
	@tornado.web.authenticated
	def render(self):
		return self.current_user

setting = dict(
	template_path=os.path.join(os.path.dirname(__file__),"templates"),
	static_path=os.path.join(os.path.dirname(__file__),"statics"),
	#ui_modules={'current_user':userModule},
	cookie_secret = "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
	#xsrf_cookies = True,
	login_url = '/',
	)

application = tornado.web.Application(
	handlers=url,debug=True,
	**setting
	)

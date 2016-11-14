#!/usr/bin/env python
#coding:utf-8
import tornado.escape
import tornado.web
import methods.db as mrd
from libraries import *
from base import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8') 

class LoginHandler(BaseHandler):
    def get(self):
        self.render("login.html",)
    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        user_pwd = mrd.select_one(table="users",column="password",condition="username",value=username)
	userPwd = tdecode(user_pwd['password'], SECRET_KEY)
        if user_pwd:
                if userPwd == password:
                        self.set_current_user(username)
			self.redirect("/file")
                else:
                        self.write("your password was not right.")
        else:
                self.write("there is no this user.")
    def set_current_user(self,user):
        if user:
                self.set_secure_cookie('user',tornado.escape.json_encode(user))
        else:
                self.clear_cookie("user")

class LogoutHandler(BaseHandler):
    def get(self):
	self.clear_cookie("user")
	self.redirect("/")

class ErrorHandler(BaseHandler):    
    def get(self):            
        self.render("error.html")

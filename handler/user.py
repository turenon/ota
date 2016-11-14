#!/usr/bin/env python
# coding=utf-8
from libraries import *
import tornado.web
import methods.db as mrd
from base import BaseHandler
class UserHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
	user_list = mrd.select_all(table="users",column="*")
	self.render('user.html',user_list=user_list)

class AddUserHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
	user = self.get_current_user().strip('"')	
	group_name_dict = mrd.select_one(table="users",column='group_name',condition='username',value=user)
	user_group = group_name_dict.get('group_name')
	if user_group == 'Admin':
		self.render("adduser.html")	
	else:
		self.render("error.html",error_info="您的账号没有权限，请联系管理员")
    def post(self):
	group_name = self.get_argument("group_name")
	username = self.get_argument("username")
	password = self.get_argument("password")
	userPwd = tencode(password, SECRET_KEY)
	#判断用户是否存在
	count_dict = mrd.select_count(table='users',condition='username',value=username)
	print count_dict.get('count(*)')
	if count_dict.get('count(*)'):
		self.render("error.html",error_info="该用户名已存在")
	else:
		insert_sql = "insert into users (group_name,username,password) values ('%s', '%s', '%s')" % (group_name,username,userPwd)
                result = mrd.insert_one(insert_sql)
                user_list = mrd.select_all(table="users",column="*")
                self.render('user.html',user_list=user_list)

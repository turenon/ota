#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import application
from handler.index import *
from handler.user import *
from handler.ota import *
url=[
    (r"/",LoginHandler),
    (r"/logout", LogoutHandler),
    (r"/file",OtaHandler),
    (r"/adduser",AddUserHandler),
    (r"/user",UserHandler),
     ]


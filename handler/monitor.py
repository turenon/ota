#!/usr/bin/env python
# coding=utf-8

import tornado.web
from base import BaseHandler

class MonitorHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render("monitor.html",)

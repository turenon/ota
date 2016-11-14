#!/usr/bin/env python
# coding=utf-8
import tornado.web
from base import BaseHandler
import os
from tornado import gen
import time
from time import sleep



class OtaHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render("ota.html")
    @tornado.web.asynchronous
    @gen.coroutine
    def post(self):
	upload_path=os.path.join(os.path.dirname(__file__),'files')  
        file_metas=self.request.files['file']    
        for meta in file_metas:
            filename=meta['filename']
            filepath=os.path.join(upload_path,filename)
            with open(filepath,'wb') as up:   
                up.write(meta['body'])
	nextBuildNumber = JenCon.server.get_job_info(taskOta)['nextBuildNumber']
	JenCon.server.build_job(taskOta,{'otaName': filename})
	i = 0
        while i<30:
                if JenCon.task_in_que(taskOta):
                        i = i + 1
                        yield gen.Task(tornado.ioloop.IOLoop.instance().add_timeout, time.time() + 1)
                        if i == 29:
                                error_info = '30秒内仍旧在队列中，请联系管理员处理异常'
                                self.render('error.html',error_info=error_info)
                                break
                else:
                        while True:
                                result = JenCon.server.get_build_info(taskOta, nextBuildNumber).get('result')
                                if not result:
                                        yield gen.Task(tornado.ioloop.IOLoop.instance().add_timeout, time.time() + 1)
                                elif result =='SUCCESS':
                                        success_info = "Ota发布成功"
                                        self.render('success.html',success_info=success_info)
                                        break
                                else:
                                        error_info = 'Ota发布失败'
                                        self.render('error.html',error_info=error_info)
                                        break
                        break
	

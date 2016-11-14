#!/usr/bin/env python
#coding:utf-8
import jenkins


class jenkinsapi():
        def __init__(self):
                self.server = jenkins.Jenkins('http://ci.gzlife.cn', username='tangwenhai', password='123456', timeout=30)
        def task_in_que(self, taskname):
                que_list = self.server.get_queue_info()
                if que_list:
                        for que in que_list:
                                if que['task']['name'] == taskname:
                                        return True
                                else:
                                        return False
                else:
                        return False

#JenCon = jenkinsapi()
if __name__ == "__main__":
        JenCon = jenkinsapi()

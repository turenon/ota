#!/usr/bin/env python
#coding:utf-8
import requests
import sys

url = "http://192.168.1.200:8888/cmdb"
def cmdb():
	html = requests.get(url)
	#return html.content
	print html.content

if len(sys.argv) == 2 and(sys.argv[1] == '--list'):
	cmdb()

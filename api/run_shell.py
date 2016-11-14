#!/usr/bin/env python
#coding:utf-8
import subprocess
def run_shell(commond):
	result = ""
	if commond:
		p = subprocess.Popen(commond,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
		result = "".join(p.stdout.readlines())
	return result
#commond='ifconfig'
#run_shell(commond)

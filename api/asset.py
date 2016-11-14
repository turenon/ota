#!/usr/bin/env python
# coding: utf-8
import sys
import os
sys.path.append("..")
import methods.db as mrd
HOMEDIR = os.path.dirname(os.path.realpath(__file__))
#SSHDIR = '/opt/d3cdemo/d3csys/d3cweb/api/key/'
SSHDIR = HOMEDIR + '/key/'


def get_asset_info(host_id):
        asset = mrd.select_one(table="hosts",column="*",condition="id",value=host_id)
	return asset

def get_user_key(user):
	#sshkey_dict = mrd.select_one(table='users',column="SSH_key",condition='username',value=user)
	key = SSHDIR + user
	return key

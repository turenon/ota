#!/usr/bin/env python
# coding=utf-8
import torndb

db = torndb.Connection("192.168.1.200:3307", "szsh", user="admin", password="123456")


def select_one(table, column, condition, value ):
    sql = "select %s from %s where %s = '%s'" % (column,table,condition,value)
    lines = db.get(sql)
    return lines
def select_count(table, condition, value):
    sql = "select count(*) from %s where %s = '%s'" % (table, condition,value)
    lines = db.get(sql)
    return lines

def select_all(table, column ):
    sql = 'select %s from %s' %(column,table)
    lines = db.query(sql)
    return lines
def select_two(table,column1,column2):
    sql = 'select %s,%s from %s' %(column1,column2,table)
    lines = db.query(sql)
    return lines

def insert_one(sql):
    db.insert(sql)

def update_one(sql):
    db.update(sql)

def del_one(sql):
    db.execute(sql)

def select_one_columns(table,column ):
    sql = 'select %s from %s'
    lines = db.get(sql,column,table)
    return lines

def insert_table(sql):
    db.insertmany(sql)

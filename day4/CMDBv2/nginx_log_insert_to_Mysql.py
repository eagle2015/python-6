#!/usr/bin/env pytthon
# -*- coding: utf8 -*-
__author__ = 'Eagle'
''' 
将nginx 日志截取后的结果，存入列表
将列表里面的数据，存入数据库
'''
import MySQLdb as mysql
import   time
log_dict = {}
log_file = file('access.txt')
for i in log_file:
    arr= i.split(' ')
    ip= arr[0]
    url = arr[6]
    status = arr[8]
    log_dict[ip,url,status] = log_dict.get((ip,url,status), 0) + 1
log_file.close()
log_list  = [(k,v) for  k,v in log_dict.items()]
log_db = mysql.connect(user='root',
                    passwd='123456',
                    db='cmdb',
                    charset="utf8",
                    host='127.0.0.1')
log_db.autocommit(True)
cur = log_db.cursor()
for s in log_list:
    ip = s[0][0]
    url = s[0][1]
    status = s[0][2]
    counts = s[1]
    sql = 'insert nginx_log  (ip,url,status,counts)values ("%s","%s",%s,%s)' % (ip,url,status,counts)
    cur.execute(sql)
cur.close()

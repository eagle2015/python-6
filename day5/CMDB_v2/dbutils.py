#!/usr/bin/env  python
#_*_ coding:utf-8 _*_
__author__ = 'Eagle'
import MySQLdb as mysql

def execute_sql(sql,tag=True):
'''# 连接数据库'''
    connect_db = mysql.connect(user='root',
                           passwd='123456',
                           db='cmdb',
                           charset="utf8",
                           host='127.0.0.1')
	# 创建游标对象
    cursor = connect_db.cursor()
	#设置两个变量默认值
    comm = None   
    rt_list =[]
    try:
        if tag:
		'''如果是查询语句,执行sql 语句，并返回数据列表'''
            comm = cursor.execute(sql)
            rt_list = cursor.fetchall()
        else:
		'''如果是曾,删，改，这三个操作，执行下面语句提交事务 '''
            comm = cursor.execute(sql)
            connect_db.commit()
    except Exception, e:
        print 'Error %s' % (sql)
       
    return comm,rt_list

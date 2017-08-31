#!/usr/bin/env  python
#_*_ coding:utf-8 _*_
__author__ = 'Eagle'
import MySQLdb as mysql
import config

connect_db = mysql.connect(
                           user   =  config.db_user,
                           passwd =  config.db_passwd,
                           db     =  config.db_name ,
                           host   =  config.db_host,
                           charset=  "utf8" )
cursor = connect_db.cursor()



# 获得注册信息，并写入数据库
def insert_sql(table_name, data,field):
    tag=False
    sql = "INSERT INTO %s (%s) VALUES (%s);" % (table_name, ','.join(field), ','.join(['"%s"' % data[x] for x in field]))
    try:
        print sql
        if  cursor.execute(sql):
             connect_db.commit()
             tag=True
    except Exception, e:
        print 'Error %s' % (sql)
    return tag

# 用户是否已存在监测
def check_user(table_name,data):
    tag=False
    try:
        sql = "select * from %s where username='%s';" % (table_name,data["username"])   
        comm = cursor.execute(sql)
        rt_list = cursor.fetchone()
        if rt_list[0] != '':
            tag=True
    except Exception, e:
        print 'Error %s' % (sql)
    return tag

# 判断用户角色
def check_role(table_name,data):
    tag=False
    values = []
    for k, v in data.items():
        values.append("%s='%s'" % (k,v))
    sql = "SELECT role  FROM %s WHERE %s ;" % (table_name,' and '.join(values))
    try:
        comm = cursor.execute(sql)
        rt_list = cursor.fetchone()
        if  rt_list[0] == 1:
            tag=True
    except Exception, e:
          print 'Error %s' % (sql)
    return tag

# 用户信息展示,分角色如果是普通用户，只显示个人信息,如果是超级管理员显示所有人信息
def user_list(table_name,data,tag=False):
    rt_list =[]
    fields = ['id','username', 'password', 'role']
    try:
        if tag:
            sql = 'select *  From %s  ; '  % (table_name)
            if  cursor.execute(sql):
                rt_list = cursor.fetchall()
                users = [dict((k,row[i]) for i,k in enumerate(fields))for row in rt_list]

        else:
            sql = 'select *  From %s where username="%s"  ; '  % (table_name,data['username'])

            print sql
            if  cursor.execute(sql):
                users = []
                rt_list = cursor.fetchone()
                users.append(dict(zip(fields,rt_list)))
    except Exception, e:
        print 'Error  SQL ERROR' 
    return  users


# 判断用户名密码是否正确
def user_authentication(table_name,data,field):
    where = []
    for k,v in data.items():
        where.append("%s='%s'" % (k, v))
    tag=False
    sql = "SELECT %s FROM %s WHERE %s ;" % (','.join(field),table_name,' and '.join(where))
    try:
        if  cursor.execute(sql):
            tag=True
    except Exception, e:
        print 'Error %s' % (sql)
    return tag

# 根据用户id 查询用户信息
def one_user_msg(table_name,id):
    tag=False
    fields=['id','username','password']
    try: 
        sql = 'SELECT  *   from %s where id=%s ;' % (table_name,id)
        print sql
        if  cursor.execute(sql):
            users = []
            rt_list = cursor.fetchone()
            users.append(dict(zip(fields,rt_list)))
            print users
            tag=True
    except Exception, e:
        print 'Error %s' % (sql)
    return users
    
# 用户数据更新
def update(table_name,data):
    tag=False
    try:
        # conditions = ["%s='%s' % (k,data[k] for k in data)"]  #更新多值
        sql = 'UPDATE  %s set password="%s" where id="%s" ;' % (table_name,data['password'],data['id'])

        if  cursor.execute(sql):
             connect_db.commit()
             tag=True
    except Exception, e:
        print 'Error %s' % (sql)
    return   tag
    
# 删除用户

def delete(table_name,data):
    tag=False
    try:
        sql = 'DELETE FROM %s where id=%s' % (table_name,data)
        if  cursor.execute(sql):
            connect_db.commit()
            tag=True
    except Exception, e:
        print 'Error %s' % (sql)
    return   tag


#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from flask import Flask,request,render_template
import MySQLdb as mysql
app = Flask(__name__)

# 连接数据库 
connect_db = mysql.connect(user='root',
                    passwd='123456',
                    db='cmdb',
                    charset="utf8",
                    host='127.0.0.1')
# 开启一个数据库提交事务
connect_db.autocommit(True)

#创建游标对象
cur = connect_db.cursor()

@app.route('/',methods=['GET', 'POST'])
def login():
'''
获取前端post 提交账号密码，查询数据库进行验证
如果用户名密码正确,则进入nginx日志界面
'''
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        sql = 'select * from usermessages where username=%s and password=md5(%s)'
        if cur.execute(sql,(username,password)):
            cur.execute('select * from nginx_log order by counts desc limit 10; ')
            nginx_log =  cur.fetchall()
            return render_template('nginx_log.html',nginx_log=nginx_log)
        else:
            error = 'User or password  Error'
            return render_template('login.html',error = error)



    return  render_template('login.html')

@app.route('/register/',methods=['GET', 'POST'])
def register():
'''  
获取前端post 提交账号，密码及重复输入密码，三个参数
如果两次密码输入正确，则提交到数据库，如果提交报错，说明用户已经存在

'''
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        if password == repassword:
            sql = 'insert  usermessages (username,password) values ("%s",md5(%s))' %  (username,password)
            try:
                cur.execute(sql)
                return "register %s successful"  % (username)
            except Exception, e:
                error = "%s already exists" % (username)
                return render_template('register.html',error=error)
    return render_template('register.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

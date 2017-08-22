#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from flask import Flask,request,render_template,redirect
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
# 创建游标对象
cur = connect_db.cursor()
@app.route('/',methods=['GET', 'POST'])
def login():
''' 登录函数: 
    获取前端post 提交账号密码，查询数据库进行验证
    如果用户名密码正确,则跳转到用户信息页面,
    否则返回登录界面，并返回错误信息'''
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        sql = 'select * from usermessages where username=%s and password=md5(%s)'
        if cur.execute(sql,(username,password)):
            return  redirect('/userlist/')
        else:
            error = u'用户名或者密码错误，请核对!'
            return render_template('login.html',error = error)
    return render_template('login.html')
            


@app.route('/userlist/',methods=['GET', 'POST'])        
def userlist():
''' 用户信息函数: 
    查询用户信息,以列表的形式返回到页面,渲染后显示'''
    sql = 'select * from usermessages ;'
    if cur.execute(sql):
        user_list =  cur.fetchall()
        index =  cur.description
        result = []
        for res in user_list:
            row = {}
            for i in range(len(index)):
                row[index[i][0]] = res[i]
            result.append(row)
    return render_template('assetlist.html',userlist=result)


@app.route('/register/',methods=['GET', 'POST'])
def register():
''' 注册函数:
    获取前端post 提交账号，密码及重复输入密码，三个参数
    如果两次密码输入正确，则提交到数据库，如果提交不一致，则返回注册页面
    如果用户已经存在，则返回用户已经存在信息 '''
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        if password == repassword:
            sql = 'insert  usermessages (username,password) values ("%s",md5(%s))' %  (username,password)
            try:
                cur.execute(sql)
                return render_template('success.html',msg=username)
            except Exception, e:
                error =  u"%s 已经存在,请使用其他用户名注册!" % (username)
                return render_template('register.html',error=error)
        else:
             error =  u"%s 两次密码不一致!" % (username)
             return render_template('register.html',error=error)
    return render_template('register.html')
@app.route('/update/',methods=['GET', 'POST'])
def  update():
''' 修改函数:
    修改操作，获取用户信息列表,用户id,然后，进入修改密码页面
    如果用户旧密码，及新密码，如果旧密码匹配，则更新密码，如果不匹配则返回错误信息'''
    if request.method=='GET':
            userid = request.args.get('id')
            return render_template('update.html',userid=userid)
    if  request.method=='POST':
        password = request.form.get('password')
        userid  = request.form.get('id')
        sql = 'select * from usermessages where id=%s and password=md5(%s)'
        if cur.execute(sql,(userid,password)):
            npassword = request.form.get('npassword')
            sql='update usermessages  set password=md5(%s) where  id=%s ;' %  (npassword,userid)
            if cur.execute(sql):
                return render_template('success1.html')
            else:
                 error = u"更新失败" 
                 return  render_template('update.html',error=error)
        else:
            error = u"旧密码错误，请重新检查！"    
            return  render_template('update.html',error=error)
              

    return  render_template('update.html')

@app.route('/delete/',methods=['GET', 'POST'])
def  delete():
''' 删除函数:
    获取用户信息列表,用户id,根据所获取的id,执行sql 删除用户操作,并返回成功页面'''
    if request.method=='GET':
        userid = int(request.args.get('id'))
        sql = 'delete from usermessages where id=%d;' % (userid)
        if cur.execute(sql):
            return render_template('success1.html',msg=userid)
    return render_template('assetlist.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from flask import Flask,request,render_template,redirect,session
from utils  import  insert_sql,check_user,check_role,user_list,user_authentication,one_user_msg,update,delete,user_list

import hashlib

salt='98b85629951ad584feaf87e28c073088'

app = Flask(__name__)

# 首页
@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')

# 用户注册函数: 
# 1.判断用户输入用户名密码是否为空
# 2.判断该用户是否存在
# 3.注册该用户信息至数据库
@app.route('/register/',methods=['GET', 'POST'])
def register():
    if request.method=='POST':
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        data['password'] = hashlib.md5(data['password']+salt).hexdigest()
        # 1.判断用户输入用户名密码是否为空
        if not data["username"] or not data["password"]:
            error = 'UserName Or Password Not Null !'
            return render_template('register.html',error=error)

        # 2.判断该用户是否存在
        elif check_user('user_messages',data):
            error = u'用户 %s 已经存在' % (data["username"])
            return render_template('register.html',error=error)

        # 3.注册该用户信息至数据库
        else:
             field = ['username','password','role']
             if  insert_sql('user_messages',data,field):
                 return redirect("/login/")

    return render_template('register.html')  

#用户登录函数
# 1. 判断用户输入用户名密码是否为空
# 2.判断用户名,密码,角色是否正确
# 3.用户角色判断，如果是管理员可查看所有用户信息，普通用户只能查看自己的信息
@app.route('/login/',methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        data= {k:v[0] for k,v in dict(request.form).items()}
        data['password'] = hashlib.md5(data['password']+salt).hexdigest()
        # 1. 判断用户输入用户名密码是否为空
        if not data["username"] or not data["password"]:
            error = 'UserName Or Password Not Null !'
            return render_template('login.html',error=error)

        # 2.判断用户名,密码,角色是否正确
        field = ['username','password','role']
        if  user_authentication('user_messages',data,field):

            # 3.用户角色判断，如果是管理员可查看所有用户信息，普通用户只能查看自己的信息
            if check_role('user_messages',data):
                users = user_list('user_messages',data,tag=True)
                return       render_template('userlist.html',userlist=users)
            else:
                users = user_list('user_messages',data,tag=False)
                return       render_template('userlist.html',userlist=users)
        else:
            error = u'用户名,或者密码错误，请核对'
            return render_template('login.html',error=error)
    return render_template('login.html')
# 用户信息更新函数
# 1.获取用户ID
# 2.用户信息更新
@app.route('/update/',methods=['GET', 'POST'])
def msg_update():
    # 1.获取用户ID
    if request.method=='GET':
        data= {k:v[0] for k,v in dict(request.form).items()}
        userid = request.args.get('id')
        users = one_user_msg('user_messages',userid)
        return render_template('update.html',userlist=users,userid=userid)
    # 2.用户信息更新
    if request.method=='POST':
        data= {k:v[0] for k,v in dict(request.form).items()}
        data['password'] = hashlib.md5(data['password']+salt).hexdigest()
        if update('user_messages',data):
            msg = u'用户信息更新成功'
            return redirect("/userlist/")
        else:
            msg = u'新密码和旧密码一致'
            return render_template('success.html',msg=msg)

    return render_template('update.html')
# 用户和列表函数
@app.route('/userlist/',methods=['GET', 'POST'])
def msg_userlist():
    users = user_list('user_messages','data',tag=True)
    return       render_template('userlist.html',userlist=users)

# 用户删除函数
# 获取用户ID 执行删除操作
@app.route('/delete/',methods=['GET', 'POST'])
def msg_delete():
    if request.method=='GET':
        data = dict((k,v[0]) for k,v in dict(request.args).items())
        
        if delete('user_messages',data['id']):
             return redirect("/userlist/")
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

#!/usr/bin/env python
# -*-coding:utf-8 -*-

from flask import request,render_template, redirect,session
from utils import  getone,check,_update,_delete,insert_sql,_center
from . import app
from sessions import sessionmsg
import json

# 用户个人中心
@app.route('/center/')
def  center():
    msg = sessionmsg()
    field  = ["id","username","name_cn","mobile","email","role"]
    data={'username':session['username']}
    result  = _center('user',data,field)
    print result
    return render_template('center.html',msg=result['msg'])

# 修改个人密码
@app.route('/user/chpwdoneself',methods=['GET', 'POST'])
def chpwdoneself():
    msg = sessionmsg()
    chpwd = {k:v[0] for k,v in dict(request.form).items()}
    where = {'id':chpwd['id'],'password':chpwd['oldpasswd']}
    field = ['id','password']
    result = check('user',field,where)
    if  result['code'] == 0:
        data =  {'id':chpwd['id'],'password':chpwd['newpasswd']}
        print  data
        result = _update('user',field,data)
    else:
        result ={'code':1, 'msg':u"旧密码不正确请重新输入!"}
    return json.dumps(result)

# 修改个人资料
@app.route('/user/chmessageoneself',methods=['GET', 'POST'])
def chmessageoneself():
    msg = sessionmsg()
    if request.method=='POST':
        field  = ["username","name_cn","mobile","email"]
        user = {k:v[0] for k,v in dict(request.form).items()}
        result = _update('user',field,user)
        if  result['code'] == 0:
            result ={'code':0, 'msg':"add user success"}
            return json.dumps(result)

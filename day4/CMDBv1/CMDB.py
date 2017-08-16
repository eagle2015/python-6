#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from flask import Flask,request,render_template

app = Flask(__name__)

# 处理nginx 日志，返回一个列表
def nginx_log_Result():
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
    result =  []
    for j  in sorted(log_list,key = lambda x:x[1], reverse=True)[:10]:
        ip= j[0][0]
        url = j[0][1]
        status = j[0][2]
        counts  = j[1]
        result.append((ip,url,status,counts))
    return  result
	
#  判断用户是否存在	
def User_already_exists(username):
        Usr_messages = file('User_messages.txt', 'rb')
        match_flag = False
        for line in Usr_messages.readlines():
            user, passwd  = line.strip(' ').split()
            if username == user :
                match_flag = True
        Usr_messages.close()
        return  match_flag

@app.route('/',methods=['GET', 'POST'])
def login():
''' 获取post提交两个参数，用户名及密码，判断登录用户名密码是否相同
		不同，返回登录界面，相同，返回nginx日志界面
		'''
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        User_messages = file('User_messages.txt')
        message=[]
        for i in User_messages:
            arry = i.split()
            message.append((arry[0],arry[1]))
        User_messages.close()
        for k in message:
            
            if k[0] == username and k[1] == password:
                nginx_log = nginx_log_Result()
                print nginx_log
                return  render_template('nginx_log.html',nginx_log=nginx_log)
   
    return  render_template('login.html')

@app.route('/register/',methods=['GET', 'POST'])
def register():
'''用户注册:获取post 表单提交用户名，密码，及重新输入密码，
三个参数， 调用函数，判断用户是否存在
如果存在打出用户已经存在信息
否则，写入用户信息，并打出注册成功页面'''

    if request.method == 'POST':
        username = request.form.get('username')
        if User_already_exists(username) == True:
            return "%s already exists" % (username)
        else:
            password = request.form.get('password')
            repassword = request.form.get('repassword')
            if password == repassword:
                User_messages = open('User_messages.txt','a+')
                User_messages.write('%s %s \n' % (username, password))
                User_messages.close()
                return  render_template('success.html',username=username)

    return render_template('register.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True)

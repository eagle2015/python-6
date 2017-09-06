#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from flask import Flask,request,render_template,redirect,session
import json
import hashlib

from utils  import    insert_sql,list,_delete,getone,_update
salt='98b85629951ad584feaf87e28c073088'

app = Flask(__name__)
app.secret_key = "98b85629951ad584feaf87e28c0730881"

# 首页
@app.route('/')

# 用户登录
@app.route('/login/',methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        data= {k:v[0] for k,v in dict(request.form).items()}
        data['password'] = hashlib.md5(data['password']+salt).hexdigest()
        field = ['id','username','password','role']
        result = getone('user',data,field)
        if  result['code'] == 0:
            session['username'] = data['username']
            session['role']  = result['msg']['role'] 
            return redirect('/darshboard/')
        else:
            return render_template('login.html',msg=result['msg'])

    return render_template('login.html')

# 仪表板：  darshboard
@app.route('/darshboard/',methods=['GET', 'POST'])
def  darshboard():
    if 'username' not in  session:
        return redirect('/login/')
    else:
        return render_template('index.html',user=session['username'],role=session['role'])

# 仪表板：  darshboard 子页面
@app.route('/darshboard/<template>')
def templates(template):
    if 'username' not in  session:
	    return redirect('/login/')

    return render_template(template)

	
# 个人中心
@app.route('/center/',methods=['GET', 'POST'])
def center():
    if 'username' not in  session:
        return redirect('/login/')
    data={'username':session['username']}
    field = ['id','username','password','role']
    result = getone('user',data,field)

    if  result['code'] == 0:
         return render_template('Personal-Center.html',msg=result['msg'])
        
    return render_template('Personal-Center.html')

#  用户列表
@app.route('/userlist/',methods=['GET', 'POST'])
def userlist():
    if 'username' not in  session:
        return redirect('/login/')
    if session['role'] == 1:
        field  = ['id','username','role']
        result = list('user',field)
        if  result['code'] == 0:
            return    render_template('user-list.html',msg=result['msg'])
    else:
        return  u"抱歉 你是普通用户没有该选项卡的权限!!!" 


# 添加用户
@app.route('/register/',methods=['GET', 'POST'])
def register():
    if request.method=='POST':
        data= {k:v[0] for k,v in dict(request.form).items()}
        data['password'] = hashlib.md5(data['password']+salt).hexdigest()
        field = ['id','username','password','role']
        result = insert_sql('user',fieald,data)
        print result
        if result['code'] == 0:
            return '用添加成功'
        else:
            return '用户添加失败'

    return       render_template('user-add.html')

#  删除用户
@app.route('/delete/',methods=['GET', 'POST'])
def delete():
    if 'username' not in  session:
        return redirect('/login/')
    if request.method=='GET':
        data = dict((k,v[0]) for k,v in dict(request.args).items())
  
        if _delete('user',data):
             return redirect("/userlist/")
    return redirect("/darshboard/")

#  用户信息修改
@app.route('/update/',methods=['GET', 'POST'])
def  update():
    if 'username' not in  session:
        return redirect('/login/')

    field = ['id','username','password','role']
    if request.method=='GET':
         userid = request.args.get('id')
         data={'id':userid}
         result = getone('user',data,field)
         print  result
         if  result['code'] == 0:
             return render_template('user-change.html',id=userid,msg=result['msg'])
    else:
        data= {k:v[0] for k,v in dict(request.form).items()}
        data['password'] = hashlib.md5(data['password']+salt).hexdigest()
        result = _update('user',field,data)
        if result['code'] == 0:
            return  '更新成功'
        else:
            return "更新失败"

    return render_template('user-change.html')




# 服务器管理列表

@app.route('/hosts/',methods=['GET', 'POST'])
def hosts():
    if 'username' not in  session:
        return redirect('/login/')

    field  = ['id','ip','username']
    result = list('host',field)
    if  result['code'] == 0:
        return    render_template('hosts.html',msg=result['msg'])
    return render_template('hosts.html')

#  添加服务器
@app.route('/addhost/',methods=['GET', 'POST'])
def addhost():
    if 'username' not in  session:
        return redirect('/login/')
  
    if request.method=='POST':
        data = dict((k,v[0]) for k,v in dict(request.form).items())

        field = ['username','password','ip']
        result = insert_sql('host',field,data)
        if result['code'] == 0:
            return '用添加成功'
        else:
            return '用户添加失败'
    return render_template('add-host.html')

# 修改服务器资料
@app.route('/updatehost/',methods=['GET', 'POST'])
def  updatehost():
    if 'username' not in  session:
        return redirect('/login/')
    field = ['id','ip','username','password']
    if request.method=='GET':
        id = request.args.get('id')
        data={'id':id}
        result = getone('host',data,field)
        
        if  result['code'] == 0:
            return render_template('update-host.html',id=id,msg=result['msg'])
    else:
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        result = _update('host',field,data)

        if result['code'] == 0:
            return  '更新成功'
        else:
            return  '更新失败'
    return render_template('update-host.html')

#  删除服务器
@app.route('/deletehost/',methods=['GET', 'POST'])
def deletehost():
    if 'username' not in  session:
        return redirect('/login/')
    if request.method=='GET':
        data = dict((k,v[0]) for k,v in dict(request.args).items())
        print data
        if _delete('host',data):
            return redirect("/hosts/")
    return redirect("/darshboard/")


#  退出用户
@app.route('/loginout/',methods=['GET', 'POST'])
def loginout():
    session.pop('username')
    return redirect('/login/')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

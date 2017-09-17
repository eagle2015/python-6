#!/usr/bin/env python
# -*-coding:utf-8 -*-

from flask import request,render_template, redirect,session
from utils import  getone,check,_update,_delete,insert_sql,list
from . import app
from sessions import sessionmsg
import json

cabinet_fields=['id','name']

idc_fields = ['id','name']

server_field = ['hostname', 'ip', 'mac', 'username', 'password', 'port', 'idc', 'brand', 'cpu', 'memory', 'disk', 'system_type', 'number', 'cabinet']
server_fields = ['id','hostname', 'ip', 'mac', 'username', 'password', 'port', 'idc', 'brand', 'cpu', 'memory', 'disk', 'system_type', 'number', 'cabinet']

# 主机列表
@app.route('/server',methods=['GET', 'POST'])
def server():
    if 'username' not in  session:
        return redirect('/login/')
    msg = sessionmsg()
    idc   =  list('idc',idc_fields)
    cabinet   = list('cabinet',cabinet_fields)
    server  = list('server',server_fields)
    idcs = idc['msg']
    cabinets =  cabinet['msg']
    servers =  server['msg']
    for cab  in servers:
        for items in cabinets:
            if  cab['cabinet'] == items['id']:
                cab['cabinet'] = items['name']
            for cac in idcs:
                if cab['idc'] == cac['id']:
                    cab['idc'] = cac['name']
    return render_template('server.html',msg=msg,server_list=server['msg'])

# 添加主机
@app.route('/serveradd',methods=['GET', 'POST'])
def serveradd():
    if 'username' not in  session:
        return redirect('/login/')
    msg = sessionmsg()
    if request.method=='GET':
        idc   =  list('idc',idc_fields)
        cabinet   =  list('cabinet',cabinet_fields)
        return render_template('serveradd.html',msg=msg,idc=idc['msg'],cabinet=cabinet['msg'])
    if request.method=='POST':
       server  = {k:v[0] for k,v in dict(request.form).items()}
       result = insert_sql('server',server_field,server)
       if  result['code'] == 0:
           result ={'code':0, 'msg':"success"}
           return  json.dumps(result)

# 更新主机信息
@app.route('/serverupdate',methods=['GET', 'POST'])
def serverupdate():
    if 'username' not in  session:
        return redirect('/login/')
    msg = sessionmsg()
    if request.method=='GET':
        id = request.args.get('id')
        data={'id':id}
        server  = getone('server',data,server_fields)
        idc   =  list('idc',idc_fields)
        cabinet   =  list('cabinet',cabinet_fields)
        print server
        return render_template('serverupdate.html',msg=msg,idc=idc['msg'],cabinet=cabinet['msg'],server_list=server['msg'])
    if request.method=='POST':
        server  = {k:v[0] for k,v in dict(request.form).items()} 
        result = _update('server',server_fields,server)
        if  result['code'] == 0:
            return  json.dumps(result)
# 删除主机
@app.route('/serverdelete',methods=['GET', 'POST'])
def serverdelete():
    if 'username' not in  session:
        return redirect('/login/')
    msg = sessionmsg()
    if request.method=='POST':
       server  = {k:v[0] for k,v in dict(request.form).items()}
 
       if _delete('server',server):
           result ={'code':0, 'msg':"delete   success"}
           return  json.dumps(result)


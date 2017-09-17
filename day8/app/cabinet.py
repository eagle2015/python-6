#!/usr/bin/env python
# -*-coding:utf-8 -*-

from flask import request,render_template, redirect,session
from utils import  getone,check,_update,_delete,insert_sql,list
from . import app
from sessions import sessionmsg
import json

field=['id','name','idc_id','u_num','power']
idc_fields = ['id','name']

# 机柜列表
@app.route('/cabinet',methods=['GET', 'POST'])
def cabinet():
    if 'username' not in  session:
        return redirect('/login/')
    msg = sessionmsg()
    idc   =  list('idc',idc_fields)
    cabinet   = list('cabinet',field)
    idcs = idc['msg']
    cabinets =  cabinet['msg']
    for cab  in cabinets:
        for items in idcs:
            if  cab['idc_id'] == items['id']:
                cab['idc_id'] = items['name']
    return render_template('cabinet.html',msg=msg,cabinet=cabinet['msg'])

# 添加机柜
@app.route('/cabinetadd',methods=['GET', 'POST'])
def cabinetadd():
    if 'username' not in  session:
        return redirect('/login/')
    msg = sessionmsg()
    if request.method=='GET':
        fields = ['id','name']
        result = list('idc',fields)
        return render_template('cabinetadd.html',msg=msg,idc=result['msg'])
    if request.method=='POST':
        cabinet  = {k:v[0] for k,v in dict(request.form).items()}
        field = ['name','idc_id','u_num','power']
        result = insert_sql('cabinet',field,cabinet)
        if  result['code'] == 0:
            result ={'code':0, 'msg':"success"}
            return  json.dumps(result)
# 更新机柜信息
@app.route('/cabinetupdate',methods=['GET', 'POST'])
def cabinetupdate():
    if 'username' not in  session:
        return redirect('/login/')
    msg = sessionmsg()
    if request.method=='GET':
        id = request.args.get('id')
        data={'id':id}
        cabinet  = getone('cabinet',data,field)
        idc  = list('idc',idc_fields)
        return render_template('cabinetupdate.html',msg=msg,cabinet=cabinet['msg'],idcs=idc['msg'])
    if request.method=='POST':
        cabinet  = {k:v[0] for k,v in dict(request.form).items()}
        result = _update('cabinet',field,cabinet)
        if  result['code'] == 0:
            result ={'code':0, 'msg':"Update  success"}
            return  json.dumps(result)
# 删除机柜
@app.route('/cabinetdelete',methods=['GET', 'POST'])
def cabinetdelete():
    if 'username' not in  session:
        return redirect('/login/')
    msg = sessionmsg()
    if request.method=='POST':
       cabinet  = {k:v[0] for k,v in dict(request.form).items()}
       if _delete('cabinet',cabinet):
           result ={'code':0, 'msg':"delete   success"}
           return  json.dumps(result)

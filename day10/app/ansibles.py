#!/usr/bin/env python
# -*-coding:utf-8 -*-
from flask import request,render_template, redirect,session
from utils import  getone,check,_update,_delete,insert_sql,list
from . import app
from sessions import sessionmsg
import json
from   commands     import   ansiblecommand
server_fields = ['id','hostname']

@app.route('/ansible',methods=['GET', 'POST'])
def ansible():
        if 'username' not in  session:
            return redirect('/login/')
        msg = sessionmsg()
        if request.method=='GET':
            server  = list('server',server_fields)            
            return render_template('ansible.html',msg=msg,server=server['msg'])

        if request.method=='POST':
            cmdmsg  = {k:v[0] for k,v in dict(request.args).items()}
            ansiblecmd = ansiblecommand(cmdmsg['cmd'],cmdmsg['pattern']) 
            pattern = cmdmsg['pattern']
            result = ansiblecmd['contacted'][pattern]['stdout']
            num = []  
            results = result.split('\n')
            for  i in range(len(results)):
                 num.append(i)
            print num
            print results
            dict_result = dict(zip(num,results))
            return json.dumps(dict_result)


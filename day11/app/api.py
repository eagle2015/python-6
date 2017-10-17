#!/usr/bin/env python
# -*-coding:utf-8 -*-

from flask import Flask,render_template,request,redirect,session
from utils import  getone,check,_update,_delete,insert_sql,list
from . import app
import json
app = Flask(__name__)
@auth.route('/api/namedadd', methods=['GET', 'POST'])
def namedadd():
    if 'username' not in  session:
        return redirect('/login/')
    msg = sessionmsg()
    if request.method=='POST':
        data= {k:v[0] for k,v in dict(request.form).items()}
        result = insert_sql('dns_records',fields,data)
        if  result['code'] == 0:
            result ={'code':0, 'msg':"Add Zone Successful"}
            return  json.dumps(result)

if __name__=='__main__':
    app.debug=True
        app.run(host='0.0.0.0',port=5001)

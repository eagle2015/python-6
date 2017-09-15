#!/usr/bin/env python
# -*-coding:utf-8 -*-
from flask import redirect,session
def sessionmsg():
    if 'username' not in  session:
        return redirect('/login/')
    msg = {'username':session['username'],'role':session['role']}
    return msg


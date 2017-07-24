# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.contrib import messages
from models import User

requestpath = "/"
newhome = '/main/'

def session(request, user):
    request.session['user'] = {
        'id' : user.id,
        'first' : user.first,
        'last' : user.last,
        'account' : user.account
    }
    return redirect(requestpath)

def sessioncheck(request, action=None):
    if 'user' in request.session:
        if request.path == requestpath:
            return redirect(newhome)
        elif request.path == requestpath + "logout":
            request.session.pop('user')
        else:
            return action
    else:
        if request.path == requestpath:
            return render(request, 'login/index.html')
    return redirect(requestpath)

def index(request):
    return sessioncheck(request)

def logout(request):
	return sessioncheck(request)

def register(request):
    if request.method == "POST":
        result = User.objects.modelreg(request)
        if result[0] == True:
            return session(request, result[1])
        else:
            for error in result[1]:
                messages.error(request, result[1][error], extra_tags=error)
    return redirect(requestpath)

def login(request):
    if request.method == "POST":
        result = User.objects.modellog(request)
        if result[0] == True:
            return session(request, result[1])
        else:
            for error in result[1]:
                messages.error(request, result[1][error], extra_tags=error)
    return redirect(requestpath)

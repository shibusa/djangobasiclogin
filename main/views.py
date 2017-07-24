# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from login.views import sessioncheck
import socket

# Create your views here.
def index(request):
    return sessioncheck(request, render(request, 'main/index.html', {"hostname": socket.gethostname()}))

# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse(u'欢迎来到首页')

def column_detail(request,column_slug):
    return HttpResponse('column slug'+column_slug)

def article_detail(request,article_slug):
    return HttpResponse('article slug'+article_slug)

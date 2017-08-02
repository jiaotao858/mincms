# -*- coding:utf-8 -*-
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *


def index(request):
    # return HttpResponse(u'欢迎来到首页')
    home_display_columns = Column.objects.filter(home_display=True)
    nav_display_columns = Column.objects.filter(nav_display=True)

    return render(request,'index.html',{
        'home_display_columns': home_display_columns,
        'nav_display_columns': nav_display_columns
    })


def column_detail(request,column_slug):
    # return HttpResponse('column slug: '+ column_slug)
    column = Column.objects.get(slug=column_slug)
    return render(request,'new/column.html',{'column':column})

def article_detail(request,pk,article_slug):
    # return HttpResponse('article slug: '+ article_slug)
    article = Article.objects.get(pk=pk)

    # if article_slug != article_slug:
    #     return redirect(article,permanent=True)

    return render(request,'new/article.html',{'article':article})
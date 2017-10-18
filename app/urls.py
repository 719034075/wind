#!usr/bin/python
#-*- coding:utf-8 _*-
from django.conf.urls import url
from . import views
app_name='app'

urlpatterns = [
    url(r'^$', views.index,name='index'),
    # url(r'^index/',views.index,name='index'),
    url(r'^searchWsd/',views.searchWsd,name='searchWsd')
]
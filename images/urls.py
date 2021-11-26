from django.urls import path
from django.conf.urls import url
from . import views

#creating the urls path

urlpatterns=[
    path('',views.welcome,name = 'welcome'),
    path('', views.welcome, name = 'index'),
    
]


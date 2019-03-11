from django.conf.urls import url
from django.urls import path

from . import views

from channels.views import new_channel, new_program

urlpatterns = [
    path('channel/create', views.new_channel, name='newchannel'),
    path('program/create', views.new_program, name='newprogram'),
    path('channel/view', views.ViewChannel.as_view(), name='viewchannel')
]
from django.conf.urls import url
from django.urls import path

from . import views

from channels.views import new_channel, new_program

urlpatterns = [
    path('channel/create', views.new_channel, name='newchannel'),
    path('program/create', views.new_program, name='newprogram'),
    path('channel/view', views.ViewChannel.as_view(), name='viewchannel'),
    url(r'program/view/(?P<id>\d+)/$', views.ViewProgram.as_view(), name='viewprogram'),
    url(r'slot/create/(?P<id>\d+)/$', views.NewSlot.as_view(), name='createslot'),
    url(r'slot/view/(?P<id>\d+)/$', views.ViewSlot.as_view(), name='viewslot'),
    path('edit/channel/<int:channel_id>/', views.ChannelUpdate.as_view(), name='editchannel'),
    path('edit/program/<int:program_id>/', views.ProgramUpdate.as_view(), name='editprogram'),
]
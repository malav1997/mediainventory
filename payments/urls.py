from django.conf.urls import url
from django.urls import path

from . import views

from payments.views import ViewAllChannels

urlpatterns = [
    path('channel/view/all', views.ViewAllChannels.as_view(), name='viewallchannel'),
    
]
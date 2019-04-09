from django.shortcuts import render
from django.views.generic import ListView

from users.models import UserProfile
from channels.models import Channel, Program, Slot

class ViewAllChannels(ListView):

	template_name= 'payments/view_allchannels.html'

	def get_queryset(self):
		queryset = Channel.objects.all()
		return queryset

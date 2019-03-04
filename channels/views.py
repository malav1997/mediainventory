from django.shortcuts import render, redirect
from django.views import generic

from users.models import UserProfile
from channels.models import Channel, Program, Slot
from channels.forms import ChannelForm


def new_channel(request):
	if request.method == 'POST':
		form = ChannelForm(request.POST)
		if form.is_valid():
			channel = form.save(commit=False)
			channel.channel_admin = request.user
			channel.save()
			return render(request, 'channels/channelsuccess.html')

	else:
		form = ChannelForm()
	return render(request, 'channels/create_channel.html', {'form': form})

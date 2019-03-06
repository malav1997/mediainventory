from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse

from users.models import UserProfile
from channels.models import Channel, Program, Slot
from channels.forms import ChannelForm, ProgramForm


def new_channel(request):
	if request.method == 'POST':
		form = ChannelForm(request.POST)
		if form.is_valid():
			channel = form.save(commit=False)
			channel.channel_admin = request.user
			channel.save()
			return render(request, 'channels/channelsuccess.html')
			#return HttpResponse('Channel Successfully Created!')

	else:
		form = ChannelForm()
	return render(request, 'channels/create_channel.html', {'form': form})

def new_program(request):
	if request.method == 'POST':
		form = ProgramForm(request.user, request.POST)
		if my_form.is_valid():
			form.save()
			return render(request, 'channels/program_success.html')

	else:
		form = ProgramForm(request.user)
	return render(request, 'channels/create_program.html', {'my_form': form})

from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.http import HttpResponse
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView


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
            # return HttpResponse('Channel Successfully Created!')

    else:
        form = ChannelForm()
    return render(request, 'channels/create_channel.html', {'form': form})


def new_program(request):

    if request.method == 'POST':
        form = ProgramForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'channels/program_success.html')

    else:
        form = ProgramForm(request.user)
    return render(request, 'channels/create_program.html', {'my_form': form})


class ViewChannel(ListView):

    template_name = 'channels/view_channel.html'

    def get_queryset(self):
        queryset = Channel.objects.filter(channel_admin=self.request.user)
        return queryset


class ViewProgram(ListView):

    template_name = 'channels/view_program.html'
    paginate_by = 1

    def get_queryset(self, **kwargs):
        id = self.kwargs['id']
        queryset = Program.objects.filter(channel=id)
        return queryset


class NewSlot(CreateView):

    model = Slot
    template_name = 'channels/create_slot.html'
    fields = ['duration', 'price']
    success_url = reverse_lazy('viewchannel')

    def dispatch(self, request, *args, **kwargs):
        self.prog = get_object_or_404(Program, pk=kwargs['id'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.prog = self.prog
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
    	
    	pk = self.request.path.split('create/')[1].replace('/', '')
    	self.prog = get_object_or_404(Program, pk=pk)
    	kwargs['program'] = self.prog
    	return super(NewSlot, self).get_context_data(**kwargs)


class ViewSlot(ListView):

	template_name = 'channels/view_slot.html'

	def get_queryset(self, **kwargs):
		pk = self.kwargs['id']
		queryset = Program.objects.filter(id=pk)
		return queryset
		

class ChannelUpdate(UpdateView):
	model = Channel
	fields = ['channel_name', 'channel_broadcaster', 'channel_desc']
	template_name='channels/edit_channel.html'
	pk_url_kwarg = 'channel_id'
	success_url = reverse_lazy('viewchannel')


class ProgramUpdate(UpdateView):
	model = Program
	fields = ['prog_name', 'channel', 'start_date', 'end_date', 'start_time', 'end_time', 'prog_desc' ]
	template_name='channels/edit_program.html'
	pk_url_kwarg='program_id'
	success_url = reverse_lazy('viewchannel')


class SlotUpdate(UpdateView):
	model = Slot
	fields = ['prog', 'duration', 'price']
	template_name = 'channels/edit_slot.html'
	pk_url_kwarg = 'slot_id'
	success_url = reverse_lazy('viewchannel') 



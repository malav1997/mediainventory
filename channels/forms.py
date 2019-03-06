from django import forms

from bootstrap_datepicker_plus import DatePickerInput

from users.models import UserProfile
from channels.models import Channel, Program, Slot


class ChannelForm(forms.ModelForm):

	class Meta:
		model = Channel
		fields= ('channel_name','channel_broadcaster', 'channel_desc',)

class ProgramForm(forms.ModelForm):

	class Meta:
		model = Program
		fields= ('prog_name', 'channel', 'start_date', 'end_date', 'start_time', 'end_time', 'prog_desc')
		widgets = {
            'start_date': DatePickerInput(), 
            'end_date': DatePickerInput(), 
        }

	def __init__(self, user, *args, **kwargs):

		super(ProgramForm, self).__init__(*args, **kwargs)
		self.fields['channel'].queryset = Channel.objects.filter(channel_admin=user)

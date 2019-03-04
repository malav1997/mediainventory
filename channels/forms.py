from django import forms

from users.models import UserProfile
from channels.models import Channel, Program, Slot


class ChannelForm(forms.ModelForm):

	class Meta:
		model = Channel
		fields= ('channel_name','channel_broadcaster', 'channel_desc',)

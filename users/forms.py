from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from users.models import UserProfile

class UserCreateForm(UserCreationForm):
	first_name=forms.CharField(required=True)
	last_name=forms.CharField(required=True)
	email=forms.EmailField(required=True)

	class Meta:
		model = UserProfile
		fields = ("first_name", "last_name", "username", "email", "password1", "password2", 'cell_no', 'user_role', )

	def save(self,commit=True):
		user=super(UserCreateForm, self).save(commit=False)
		user.email=self.cleaned_data["email"]
		user.first_name=self.cleaned_data["first_name"]
		user.last_name=self.cleaned_data["last_name"]
		if commit:
			user.save()
		return user


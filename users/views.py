from django.shortcuts import render
from django.contrib.auth import login, authenticate
#from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from users.forms import UserCreateForm

# Create your views here.
def home_page(request):
    return render(request, 'users/home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, 'users/home.html')
    else:
        form = UserCreateForm()
    return render(request, 'users/signup.html', {'form': form})


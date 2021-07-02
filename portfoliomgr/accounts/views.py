from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from django.contrib import messages

# Create your views here.
from .forms import CreateUserForm

def index(request):
    return HttpResponse("Accounts page")

def register_page(request):
    form = CreateUserForm

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user_email = form.cleaned_data.get('email')
            messages.info(request, 'Please confirm registration by clicking activation link sent to {}'.format(user_email))
            return redirect('login')

    context = {'form':form}
    return render(request, 'accounts/register.html', context)

def login_page(request):
    context = {}
    return render(request, 'accounts/login.html', context)
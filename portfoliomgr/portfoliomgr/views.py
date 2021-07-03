from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def index(request):
    context = {}
    return render(request, 'main.html', context)

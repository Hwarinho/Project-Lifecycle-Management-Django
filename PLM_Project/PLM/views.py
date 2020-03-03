import subprocess
import sys

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib.auth.models import User


def index(request):
    return render(request, 'home/index.html')


def signup(request):
    if request.method == "POST":
        form = UserRegisterForm()
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = User.objects.create_user(username=username, password=password)
            messages.success(request, 'Account created successfully')
            login(request, user)
            return redirect('Dashboard')
    else:
        form = UserRegisterForm()
    return render(request, 'sign-up/signup.html', {'form': form})


def login(request):
    return render(request, 'login/login.html')


def dashboard(request):
    return render(request, 'dashboard/mainPage.html')


def profile(request):
    return render(request, 'profile/profile.html')


def projectCreation(request):
    return render(request, 'project/projectCreation.html')

def FAQ(request):
    return render(request, 'extras/faq.html')
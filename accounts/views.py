# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.shortcuts import render,redirect
from boards.models import Category
from .forms import SignUpForm

# Create your views here.

def signup(request):
    categories= Category.objects.all()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    ctx = {
        'form': form,
        'categories':categories,
        }
    return render(request, 'technews/signup.html', ctx )

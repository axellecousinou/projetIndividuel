from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def log(request):
    return redirect('accounts/login')


@login_required()
def newsfeed(request):
    return render(request, 'communitymanager/newsfeed.html')


def disconnect(request):
    return redirect('accounts/logout')

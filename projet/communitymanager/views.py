from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Communaute


def log(request):
    return redirect('newsfeed')


@login_required()
def newsfeed(request):
    return render(request, 'communitymanager/newsfeed.html')


def disconnect(request):
    return redirect('accounts/logout')


def communautes(request):
    list = Communaute.objects.all()
    return render(request, 'communitymanager/communaute-list.html', locals())


def desabonnement(request, com_id):
    c = Communaute.objects.get(id=com_id)
    c.abonnes.remove(request.user)
    return redirect('communautes')


def abonnement(request, com_id):
    c = Communaute.objects.get(id=com_id)
    c.abonnes.add(request.user)
    return redirect('communautes')

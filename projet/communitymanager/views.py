from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Communaute
from .models import Post
from .forms import NewPostForm
from datetime import datetime


def log(request):
    return redirect('newsfeed')


@login_required()
def newsfeed(request):
    return render(request, 'communitymanager/newsfeed.html')


def disconnect(request):
    return redirect('accounts/logout')


@login_required()
def communautes(request):
    list = Communaute.objects.all()
    return render(request, 'communitymanager/communaute-list.html', locals())


@login_required()
def desabonnement(request, com_id):
    c = Communaute.objects.get(id=com_id)
    c.abonnes.remove(request.user)
    return redirect('communautes')


@login_required()
def abonnement(request, com_id):
    c = Communaute.objects.get(id=com_id)
    c.abonnes.add(request.user)
    return redirect('communautes')


@login_required()
def communaute(request, com_id):
    list = Post.objects.all()
    com = Communaute.objects.get(id=com_id)
    return render(request, 'communitymanager/communaute.html', locals())


@login_required()
def post_details(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'communitymanager/post-details.html', locals())


@login_required()
def create_post(request):
    form = NewPostForm(request.POST or None)
    if form.is_valid():
        post = Post()
        print(post)
        post.titre = form.cleaned_data['titre']
        post.description = form.cleaned_data['description']
        post.communaute = form.cleaned_data['communaute']
        post.priorite = form.cleaned_data['priorite']
        post.evenementiel = form.cleaned_data['evenementiel']
        if post.evenementiel:
            post.date_evenement = form.cleaned_data['date_evenementiel']
        post.date_creation = datetime.now()
        post.auteur = request.user
        post.save()

        return redirect('communaute', com_id=post.communaute.id)

    return render(request, 'communitymanager/post-creation.html', locals())


@login_required()
def modif_post(request, post_id):
    form = NewPostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.auteur = request.user
        post.date_creation = datetime.now()
        return redirect('details', post_id=post_id)
    else:
        p = get_object_or_404(Post, id=post_id)
        form = NewPostForm(instance=p)
        return render(request, 'communitymanager/modify-post.html', locals())


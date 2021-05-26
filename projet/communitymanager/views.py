from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Communaute
from .models import Post
from .models import Commentaire
from .models import Priorite
from .forms import NewPostForm
from .forms import NewCommentForm
from datetime import datetime


def log(request):
    return redirect('communautes')


@login_required()
def newsfeed(request):
    communautes = request.user.communaute_set.all()
    list = []
    for com in communautes:
        l = Post.objects.filter(communaute=com).order_by('date_creation').reverse()
        for p in l:
            list.append(p)
    return render(request, 'communitymanager/newsfeed.html', locals())


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
    list = Post.objects.filter(communaute=Communaute.objects.get(id=com_id))
    com = Communaute.objects.get(id=com_id)
    return render(request, 'communitymanager/communaute.html', locals())


@login_required()
def post(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = Commentaire.objects.filter(post = post)
    form = NewCommentForm(request.POST or None)
    if form.is_valid():
        commentaire = form.save(commit=False)
        commentaire.date_creation = datetime.now()
        commentaire.auteur = request.user
        commentaire.post = post
        commentaire.save()
        return redirect('post', post_id)
    return render(request, 'communitymanager/post-details.html', locals())


@login_required()
def nouveau_post(request):
    form = NewPostForm(request.POST or None)
    prio = Priorite.objects.all()
    communautes = request.user.communaute_set.all()
    if form.is_valid():
        post = form.save(commit=False)
        post.evenementiel, post.date_evenement = form.clean_evenement_date(request)
        post.date_creation = datetime.now()
        post.auteur = request.user
        print(post.date_evenement)
        try :
            post.save()
            return redirect('communaute', com_id=post.communaute.id)
        except:
            date = True
            return render(request, 'communitymanager/post-creation.html', locals())

    return render(request, 'communitymanager/post-creation.html', locals())


@login_required()
def modif_post(request, post_id):
    p = get_object_or_404(Post, id=post_id)
    if p.auteur == request.user:
        form = NewPostForm(request.POST or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.auteur = request.user
            post.date_creation = datetime.now()
            return redirect('post', post_id=post_id)
        else:
            form = NewPostForm(instance=p)
            return render(request, 'communitymanager/modify-post.html', locals())
    else :
        list = Post.objects.filter(communaute=Communaute.objects.get(id=Post.objects.get(id=post_id).communaute.id))
        can_modif = True
        return render(request, 'communitymanager/communaute.html', locals())


@login_required()
def suppress_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.auteur == request.user:
        com_id = post.communaute.id
        post.delete()
        return redirect('communaute', com_id=com_id)
    else :
        list = Post.objects.filter(communaute=Communaute.objects.get(id=Post.objects.get(id=post_id).communaute.id))
        can_suppress = True
        return render(request, 'communitymanager/communaute.html', locals())


@login_required()
def voir_commentaires(request, post_id):
    post = Post.objects.get(id=post_id)
    commentaires = Commentaire.objects.filter(post=post)
    voir_comm = True
    communautes = request.user.communaute_set.all()
    list = []
    for com in communautes:
        l = Post.objects.filter(communaute=com).order_by('date_creation').reverse()
        for p in l:
            list.append(p)
    return render(request, 'communitymanager/newsfeed.html', locals())


@login_required()
def post_commentaire(request, post_id):
    form = NewCommentForm(request.POST or None)
    if form.is_valid():
        commentaire = form.save(commit=False)
        commentaire.auteur = request.user
        commentaire.date_creation = datetime.now()
        commentaire.post = get_object_or_404(Post, id=post_id)
        commentaire.save()
        return redirect('voir-commentaires', post_id=post_id)
    return render(request, 'communitymanager/newsfeed.html', locals())
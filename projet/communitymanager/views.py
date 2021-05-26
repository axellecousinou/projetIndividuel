from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Communaute
from .models import Post
from .models import Commentaire
from .models import Priorite
from .forms import NewPostForm
from .forms import NewCommentForm
from datetime import datetime


@login_required()
def newsfeed(request):
    """
    Renvoie l'ensemble des posts dont la communauté appartient à la liste des communautés de l'utilisateur
    """
    communautes = request.user.communaute_set.all()
    list = Post.objects.filter(Q(communaute__in=communautes)).order_by('date_creation').reverse()
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
    comments = Commentaire.objects.filter(post=post)
    form = NewCommentForm(request.POST or None)
    if form.is_valid():
        #On n'enregistre pas directement le form car certains éléments automatiques doivent être ajoutés au form
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

        #On récupère ces deux éléments sous une forme de date pour pouvoir enregistrer le post
        post.evenementiel, post.date_evenement = form.clean_evenement_date(request)
        post.date_creation = datetime.now()
        post.auteur = request.user
        post.save()
        return redirect('communaute', com_id=post.communaute.id)
    #Si le form n'est pas valide on renvoie la vue de création de post
    return render(request, 'communitymanager/post-creation.html', locals())


@login_required()
def modif_post(request, post_id):
    #On commence par récupérer le post d'origine pour pouvoir rentrer ses valeurs dans le form
    p = get_object_or_404(Post, id=post_id)

    #Si l'utilisateur en est bien l'auteur alors il a le droit de le modifier
    if p.auteur == request.user:
        form = NewPostForm(request.POST or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.auteur = request.user
            #La date de création est mise à jour à la date de la modification
            post.date_creation = datetime.now()
            return redirect('post', post_id=post_id)
        else:
            form = NewPostForm(instance=p)
            return render(request, 'communitymanager/modify-post.html', locals())
    else :
        #Si jamais l'utilisateur n'est pas l'auteur on doit récupérer l'ensemble des posts et ajouter une variable pour
        # pouvoir afficher un message d'erreur
        list = Post.objects.filter(communaute=Communaute.objects.get(id=Post.objects.get(id=post_id).communaute.id))
        can_modif = True
        return render(request, 'communitymanager/communaute.html', locals())


@login_required()
def suppress_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    #Seul l'auteur du post peut le supprimer
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
    """
    Cette méthode est appelée quand un utilisateur sur la page newsfeed veut voir les commentaires d'un
    post en particulier
    """
    post = Post.objects.get(id=post_id)
    commentaires = Commentaire.objects.filter(post=post)
    voir_comm = True
    communautes = request.user.communaute_set.all()
    list = Post.objects.filter(Q(communaute__in=communautes)).order_by('date_creation').reverse()
    return render(request, 'communitymanager/newsfeed.html', locals())



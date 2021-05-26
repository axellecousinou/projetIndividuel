from django.urls import path
from . import views


urlpatterns = [
    path('newsfeed/', views.newsfeed, name='newsfeed'),
    path('communautes/', views.communautes, name='communautes'),
    path('', views.log),
    path('desabonnement/<int:com_id>', views.desabonnement, name='desabonnement'),
    path('abonnement/<int:com_id>', views.abonnement, name='abonnement'),
    path('communaute/<int:com_id>', views.communaute, name='communaute'),
    path('post/<int:post_id>', views.post, name='post'),
    path('nouveau_post/', views.nouveau_post, name='nouveau-post'),
    path('modif_post/<int:post_id>', views.modif_post, name='modif-post'),
    path('suppress_post/<int:post_id>', views.suppress_post, name='suppress-post'),
    path('voir_commentaires/<int:post_id>', views.voir_commentaires, name='voir-commentaires'),
    path('post_commentaire/<int:post_id>', views.post_commentaire, name='post-commentaire'),
]

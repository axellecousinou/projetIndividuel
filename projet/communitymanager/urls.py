from django.urls import path
from . import views


urlpatterns = [
    path('newsfeed/', views.newsfeed, name='newsfeed'),
    path('communautes/', views.communautes, name='communautes'),
    path('', views.log),
    path('desabonnement/<int:com_id>', views.desabonnement, name='desabonnement'),
    path('abonnement/<int:com_id>', views.abonnement, name='abonnement'),
]

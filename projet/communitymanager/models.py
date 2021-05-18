from django.db import models
from django.contrib.auth.models import User


class Communaute(models.Model):
    nom = models.CharField(max_length=40)
    abonnes = models.ManyToManyField(User)


class Priorite(models.Model):
    label = models.CharField(max_length=20)


class Post(models.Model):
    titre = models.CharField(max_length=30)
    description = models.TextField()
    date_creation = models.DateTimeField()
    communaute = models.ForeignKey(Communaute, on_delete=models.CASCADE)
    priorite = models.ForeignKey(Priorite, on_delete=models.CASCADE)
    evenementiel = models.BooleanField()
    date_evenement = models.DateTimeField()
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)

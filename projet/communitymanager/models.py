from django.db import models
from django.contrib.auth.models import User


class Communaute(models.Model):
    nom = models.CharField(max_length=40)
    abonnes = models.ManyToManyField(User)

    def __str__(self):
        return self.nom


class Priorite(models.Model):
    label = models.CharField(max_length=20)

    def __str__(self):
        return self.label


class Post(models.Model):
    titre = models.CharField(max_length=30)
    description = models.TextField()
    date_creation = models.DateTimeField()
    communaute = models.ForeignKey(Communaute, on_delete=models.CASCADE)
    priorite = models.ForeignKey(Priorite, on_delete=models.CASCADE)
    evenementiel = models.BooleanField()
    date_evenement = models.DateTimeField(blank=True, null=True)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titre


class Commentaire(models.Model):
    date_creation = models.DateTimeField()
    contenu = models.CharField(max_length=300)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

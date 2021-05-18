from django.db import models
from django.contrib.auth.models import User


class Communaute(models.Model):
    nom = models.CharField(max_length=40)
    abonnes = models.ManyToManyField(User)

from django.db import models
from django.contrib.auth.models import User


class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    abonnements = []

    def __str__(self):
        return "Profil de {0}".format(self.user.username)

from django import forms
from .models import Post
from .models import Commentaire


class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('date_creation', 'auteur')


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ('contenu',)

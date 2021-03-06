from django import forms
from .models import Post
from .models import Commentaire


class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('date_creation', 'auteur', 'evenementiel', 'date_evenement')

    def clean_evenement_date(self, request):
        #Le format de la date n'est désormais plus le bon et il faut donc le remettre au bon format pour qu'il
        # soit accepté lors de la sauvegarde de l'objet
        if request.POST.get('evenementiel'):
            evenementiel = True
            date = request.POST.get('date_evenement')
            date_evenement = ""
            for i in range(len(date)):
                if date[i] == 'T':
                    date_evenement += ' '
                else:
                    date_evenement += date[i]
            return evenementiel, date_evenement
        else:
            return False, None



class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ('contenu',)

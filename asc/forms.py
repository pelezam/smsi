from django import forms
from .models import Asc


class AscForm(forms.ModelForm):

    class Meta:
        model = Asc
        fields = (
            'identifiant',
            'ancien_id',
            'nom',
            'prenom',
            'sexe',
            'site',
            'type',
            'contact',
            'photo',
            )

from django import forms
from .models import Equipement, Approvisionnement
from django.core.exceptions import ValidationError


class EquipmentForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 2}), required=False)

    class Meta:
        model = Equipement
        fields = '__all__'

    def clean_libelle(self):
        libelle = self.cleaned_data['libelle']
        return libelle.lower()

    def clean_echeance(self):
        echeance = int(self.cleaned_data['echeance'])
        if echeance <= 0:
            raise ValidationError("l'écheance doit être supérieur à 0")
        return echeance


class ApproForm(forms.ModelForm):

    class Meta:
        model = Approvisionnement
        fields = ('equipement', 'quantity_add',)

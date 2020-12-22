from django import forms
from .models import Attribution, AttributionSite
from attribution.models import Attribution
from asc.models import Asc
from django.core.exceptions import ValidationError


class AttibutionForm(forms.ModelForm):

    class Meta:
        model = Attribution
        fields = ('asc', 'equipement', 'quantity')

    def clean(self):
        errors = {}
        data = self.cleaned_data
        quantity = data.get('quantity')
        equipement = data.get('equipement')
        asc = data.get('asc')

        if Attribution.objects.filter(asc=asc, equipement=equipement).count() > 0:
            errors['equipement'] = ["Cet équipement à déjà été attribué"]

        if equipement.quantity < int(quantity):
            errors['quantity'] = ["La quantité disponible ne permet pas de faire cette opération"]
        
        if errors:
            raise ValidationError(errors)

        return data


class AttributionSiteForm(forms.ModelForm):

    class Meta:
        model = AttributionSite
        fields = ('site', 'equipement', 'quantity')

    def clean(self):
        data = self.cleaned_data
        site = data.get('site')
        quantity = data.get('quantity')
        equipement = data.get('equipement')

        nb_asc = Asc.objects.filter(site=site).count()

        qte_demander = int(nb_asc) * int(quantity)

        if equipement.quantity < qte_demander:
            raise forms.ValidationError('La quantité disponible ne permet pas de faire cette opération')

        return data

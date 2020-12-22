from django import forms
from .models import Site


class SiteForm(forms.ModelForm):

    class Meta:
        model = Site
        fields = ('district', 'libelle', )

    def clean_libelle(self):
        libelle = self.cleaned_data['libelle']
        return libelle.lower()

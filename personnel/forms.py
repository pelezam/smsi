from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Personnel


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = Personnel
        fields = ('last_name', 'first_name', 'contact', 'sexe', 'fonction')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Personnel
        fields = ('last_name', 'first_name', 'contact', 'sexe', 'fonction')
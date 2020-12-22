from django.shortcuts import render
from django.views.generic import CreateView
from .models import *


class PersonnelCreateView(CreateView):
    model = Personnel
    fields = ('last_name', 'first_name', 'sexe', 'fonction', 'contact')
    template_name = 'index.html'

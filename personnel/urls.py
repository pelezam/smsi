from django.urls import path
from django.views.generic import TemplateView
from .views import PersonnelCreateView

urlpatterns = [
    path('', PersonnelCreateView.as_view(), name='personnel_list'),
]
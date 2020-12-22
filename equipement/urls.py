from django.urls import path
from . import views

app_name = "equipement"

urlpatterns = [
    path('', views.equipement_list, name="list"),
    path('create/', views.equipement_create, name="create"),
    path('<int:id>/edit/', views.equipement_edit, name="edit"),
    path('<int:id>/detail/', views.equipement_detail, name="detail"),
    path('<int:id>/approvisionement/detail/', views.approvisionement_list, name="approvisionement_list"),
    path('approvisionement/', views.approvisionement_create, name="appro_create"),
]
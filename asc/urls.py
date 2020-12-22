from django.urls import path
from . import views
app_name = 'asc'

urlpatterns = [
    path('', views.asc_list, name="asc_list"),
    path('<str:id>/detail/', views.asc_detail, name="asc_detail"),
    path('<str:id>/edit/', views.asc_edit, name="asc_edit"),
    path('<str:id>/attribution/', views.asc_attribution, name="asc_attributon"),
    path('<str:id>/attribution/<int:id_attr>/delete/', views.asc_attribution_delete, name="asc_attribution_delete"),
    path('create/', views.asc_create, name="asc_create"),
]
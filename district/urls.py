from django.urls import path
from . import views

app_name = "district"

urlpatterns = [
    path('sites/', views.site_list, name="site_list"),
    path('create/', views.site_create, name="site_create"),
    path('sites/<int:id>/detail/', views.site_detail, name="site_detail"),
    path('sites/<int:id>/edit/', views.site_edit, name="site_edit"),
]
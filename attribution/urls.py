from django.urls import path
from . import views

app_name = "attribution"

urlpatterns = [
    path('<int:id>/detail/', views.attribution_detail, name="detail")
]
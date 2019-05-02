from django.urls import path
from . import  views

app_name = "main"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("details/<int:medicine_id>/", views.details, name="detail")
]

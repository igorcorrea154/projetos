from django.urls import path
from blog import views

urlpatterns = [
    path('inicio/', views.inicio, name = "inicio"),
    path('sobre/', views.sobre, name="sobre")
]

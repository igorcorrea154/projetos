from django.contrib import admin
from django import views
from django.urls import path, include
from gerenciamento_tarefas import views as contas_views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('contas/', include('gerenciamento_tarefas.urls')),
    path('home', contas_views.home, name='home'),
]

from . import views
from django.urls import path

urlpatterns = [
    path('cadastro/',views.cadastro, name='cadastro'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('home/',views.home, name='home'),
    path('tarefas/', views.lista_tarefas, name='lista_tarefas'),
    path('tarefas/nova/', views.criar_tarefa, name='criar_tarefa'),
]
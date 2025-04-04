from django.contrib import admin
from django.urls import path
from graf_site import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.linkvertise_page, name='linkvertise_page'),
    path('meu-token/', views.mostrar_token, name='mostrar_token'),

]

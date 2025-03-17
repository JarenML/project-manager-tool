from django.urls import path
from . import views

urlpatterns = [
    #path('', views.home, name='home'),
    #path('private_home/', views.private_home, name="private_home"),
    path('registro/', views.registrar_usuario, name="registrar_usuario"),
]

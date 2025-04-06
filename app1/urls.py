from django.urls import path
from . import views

urlpatterns = [
    path('', views.public_home, name='public_home'),
    path('private_home/', views.private_home, name="private_home"),
    path('registro/', views.registrar_usuario, name="registrar_usuario"),
    path('login/', views.login_user, name='login_user'),
]

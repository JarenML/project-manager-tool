from django.urls import path
from . import views

urlpatterns = [
    path('', views.public_home, name='public_home'),
    path('private_home/', views.private_home, name="private_home"),
    path('registro/', views.register_user, name="register_user"),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user')
]

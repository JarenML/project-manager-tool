from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegister(forms.Form):
    first_name = forms.CharField(label='Ingresa tu nombre',
                                 widget=forms.TextInput(attrs={'placeholder': 'Tu nombre'}))

    last_name = forms.CharField(label='Ingresa tu apellido',
                                widget=forms.TextInput(attrs={'placeholder': 'Tu apellido'}))

    email = forms.EmailField(label='Ingresa tu email',
                             widget=forms.EmailInput(attrs={'placeholder': 'Tu email'}))
    username = forms.CharField(label='Ingresa tu nombre de usuario para la plataforma',
                               widget=forms.TextInput(attrs={'placeholder': 'Tu usuario'}))

    password1 = forms.CharField(label='Ingresa tu contraseña',
                                widget=forms.PasswordInput(attrs={'placeholder': 'Tu contraseña'}))
    password2 = forms.CharField(label='Confirma tu contraseña',
                                widget=forms.PasswordInput(attrs={'placeholder': 'Tu confirmacion'}))


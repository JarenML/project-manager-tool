from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.messages import success
from django.http import HttpResponse


# Create your views here.
def registrar_usuario(request):
    if request.method == "GET":
        form = UserCreationForm()
        return render(request, 'app1/login.html', {'form': form})

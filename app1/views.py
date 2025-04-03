from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .forms import UserRegister
from django.contrib.auth.models import User
from django.db.utils import IntegrityError


# Create your views here.
def registrar_usuario(request):
    if request.method == "GET":
        form = UserRegister()
        return render(request, 'app1/register.html', {'form': form})
    else:
        form = UserRegister(request.POST)
        if form.is_valid():
            username_cleaned = form.cleaned_data["username"]
            password1_cleaned = form.cleaned_data["password1"]
            password2_cleaned = form.cleaned_data["password2"]

            if password1_cleaned != password2_cleaned:
                messages.success(request, "Las contraseñas no coinciden")
                return render(request, 'app1/register.html', {'form': form})
            try:
                user = User.objects.create_user(username=username_cleaned, password=password1_cleaned)
                user.save()
                login(request, user)
                return redirect('private_home')
            except IntegrityError:
                messages.success(request, "Error: Posible duplicidad en los datos")

        return render(request, 'app1/register.html', {'form': form})


def login_user(request):
    if request.method == "GET":
        form = AuthenticationForm()
        return render(request, 'app1/login.html', {'form': form})


def private_home(request):
    return HttpResponse(f"Este es el panel privado: Bienvenido {request.user}")

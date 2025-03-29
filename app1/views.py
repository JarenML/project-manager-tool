from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.messages import success
from django.http import HttpResponse


# Create your views here.
def registrar_usuario(request):
    if request.method == "GET":
        form = UserCreationForm()
        return render(request, 'app1/login.html', {'form': form})
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username_cleaned = form.cleaned_data["username"]
            password_cleaned = form.cleaned_data["password1"]
            user = authenticate(username=username_cleaned, password=password_cleaned)
            if user is not None:
                login(request, user)
                return redirect('private_home')

        success(request, "Vuelve a intentarlo!")
        return render(request, 'app1/login.html', {'form': form})


def private_home(request):
    return HttpResponse(f"Este es el panel privado: Bienvenido {request.user}")

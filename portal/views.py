from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrarUsuarioForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


def index(request):
    return render(request,'portal/index.html',{})


def login_usuario(request):
    if request.method == 'POST':
        # AuthenticationForm_can_also_be_used__
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' Bienvenido/a {username} !!')
            return redirect('portal')
        else:
            messages.error(request, f'Cuenta o password incorrecto, realice el login correctamente')
    form = AuthenticationForm()
    return render(request, 'portal/login.html', {'form': form})

    return render(request,'portal/login.html',{})

def registrarse(request):
    if request.method == 'POST':
        form = RegistrarUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrarUsuarioForm()
    

    return render(request,'portal/registrarse.html',{'form':form})

def logout(request):
    pass
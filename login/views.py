from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,"login.html")

def index(request):
    return render(request,"index.html")

def empresa(request):
    return render(request, "empresa.html")

def mantenimiento(request):
    return render(request, "mantenimiento.html")

def menuAspel(request):
    return render(request, "menuAspel.html")

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def login_user(request):
    if request.method == 'POST':
        username = request.POST['admin']
        password = request.POST['admin']

        # Autenticar al usuario con las credenciales proporcionadas
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # El usuario es autenticado, iniciar sesión
            login(request, user)
            return redirect('inicioAdmin')
        else:
            # El usuario no es autenticado, mostrar un mensaje de error
            messages.error(request, 'El nombre de usuario o contrseña no son correctos.')
            return redirect('login')

    else:
        return render(request, 'login.html')
def logout_user(request):
    # Cerrar sesión del usuario
    logout(request)
    return redirect('login')
 
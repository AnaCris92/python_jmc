from django.shortcuts import render

# Create your views here.
def mantenimiento(request):
    return render(request,"mantenimiento.html")

def index(request):
    return render(request,"index.html")

def empresa(request):
    return render(request, "empresa.html")

def sWeb(request):
    return render(request, "sWeb.html")

def menuAspel(request):
    return render(request, "menuAspel.html")

def login(request):
    return render(request, "login.html")
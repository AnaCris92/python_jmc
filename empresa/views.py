from django.shortcuts import render

# Create your views here.
def empresa(request):
    return render(request,"empresa.html")

# Create your views here.
def index(request):
    return render(request,"index.html")

def mantenimiento(request):
    return render(request, "mantenimiento.html")

def sWeb(request):
    return render(request, "sWeb.html")

def menuAspel(request):
    return render(request, "menuAspel.html")
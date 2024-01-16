from django.shortcuts import render

# Create your views here.
def sWeb(request):
    return render(request,"sWeb.html")

def index(request):
    return render(request,"index.html")

def empresa(request):
    return render(request, "empresa.html")

def mantenimiento(request):
    return render(request, "mantenimiento.html")

def menuAspel(request):
    return render(request, "menuAspel.html")




from django.shortcuts import render

# Create your views here.
def menuAspel(request):
    return render(request,"menuAspel.html")

def sae(request):
    return render(request, "sae.html")

def coi(request):
    return render(request, "coi.html")

def noi(request):
    return render(request, "noi.html")

def adm(request):
    return render(request, "adm.html")

def caja(request):
    return render(request, "caja.html")

def prod(request):
    return render(request, "prod.html")

def facture(request):
    return render(request, "facture.html")

def banco(request):
    return render(request, "banco.html")

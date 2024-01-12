from django.shortcuts import render

# Create your views here.
def menuAspel(request):
    return render(request,"menuAspel.html")

def sae(request):
    return render(request, "sae.html")
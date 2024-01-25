from django.shortcuts import render

# Create your views here.
def inicio_cliente(request):
    return render(request,"inicio_cliente.html")
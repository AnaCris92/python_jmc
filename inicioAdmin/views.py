from django.shortcuts import render

# Create your views here.
def inicioAdmin(request):
    return render(request,"inicioAdmin.html")

def control_clientes(request):
    return render(request, "control_clientes.html")


from django.shortcuts import render

# Create your views here.
def inicioAdmin(request):
    return render(request,"inicioAdmin.html")

def control_clientes(request):
    return render(request, "control_clientes.html")

def control_contratos(request):
    return render(request, "control_contratos.html")

def control_soporte(request):
    return render(request, "control_soporte.html")

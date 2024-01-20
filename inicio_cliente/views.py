from django.shortcuts import render

# Create your views here.
def inicio_cliente(request):
    return render(request,"inicio_cliente.html")

def equipo_cliente(request):
    return render(request, "equipo_cliente.html")

def tickets_cliente(request):
    return render(request, "tickets_cliente.html")

def contratos_cliente(request):
    return render(request, "contratos_cliente.html")

def pagos_cliente(request):
    return render(request, "pagos_cliente.html")
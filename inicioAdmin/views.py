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

def control_pagos(request):
    return render(request, "control_pagos.html")

def control_ajuste(request):
    return render(request, "control_ajuste.html")

def equipo_cliente(request):
    return render(request, "equipo_cliente.html")

def tickets_cliente(request):
    return render(request, "tickets_cliente.html")

def contratos_cliente(request):
    return render(request, "contratos_cliente.html")

def pagos_cliente(request):
    return render(request, "pagos_cliente.html")

def control_staff(request):
    return render(request, "control_staff.html")

from django.shortcuts import render #funciones de django
from .forms import ClienteForm #traer el formulario de cliente de la app
from django.contrib import messages#se utiliza para mostrar mensajes
from .models import Cliente #importa el modelo de cliente de la app
from django.shortcuts import render, get_object_or_404, redirect  #indica que va a recuperar un argumento y va a devolver un httpresponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def create_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)  # Vincula el formulario con los datos POST
        if form.is_valid():
            form.save() # Guarda los datos en la base de datos
            messages.success(request, 'Cliente creado con exito.') # Muestra un mensaje de éxito
            return redirect('listar') # Redirige a la página de listado de los clientes
        else:
            messages.error(request, 'Error al insertar datos. Revise los datos.')
            messages.error(request, form.errors)  # Agrega mensajes de error detallados
    else:
        form = ClienteForm()  # Crea un objeto vacío 
    return render(request, 'control_clientes.html', {'form': form})# Renderiza la plantilla HTML con el formulario

#funcion para mostrar la lista de los clientes
def listar_cliente(request): #hacemos la solicitud al servidor con la funcion request
    clientes = Cliente.objects.all() #mostramos los clientes almacenaso en la base de datos
    return render (request, "control_clientes.html", {"clientes":clientes}) #respuesta del servidor en la pagina control-clientes

#funcion para actualizar o modificar los datos del cliente
def update_cliente(request, id_cliente): #obtener los datos del cliente mediante el id
    cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
    if request.method == 'POST': #revisa si la solicitud es post y puede enviar los nuevos datos
        form = ClienteForm(request.POST, instance=cliente) #se crea el formulario para la validacion
        if form.is_valid():
            form.save()#si son validos se guardan 
            data = {'message': 'Datos actualizados correctamente'} 
            return redirect('listar') #se regresa al la pagina donde estan los clientes
        else:
            data = {'error': 'Error al actualizar datos. Revise los datos.'}
            return JsonResponse(data)
    else:
        data = {
            'nombre':cliente.nombre,
            #'correo': cliente.correo,
            #'direccion':cliente.direccion,
            #'telefono': cliente.telefono,
            #'rfc':cliente.rfc,
            #'cp':cliente.cp,
            #'municipio': cliente.municipio,
            #'estado': cliente.estado,
            #'nom_contacto': cliente.nom_contacto,
        }
        
        return JsonResponse(data)#toma los datos almacenado y los envia  a donde se ralizo la solicitud

@csrf_exempt # desactiva la protección CSRF para que se pueda eliminar registros
def delete_cliente(request, id_cliente):
    if request.method == 'POST':
        try:
            cliente = get_object_or_404(Cliente, id_cliente=id_cliente) 
            cliente.delete()
            return JsonResponse({'message': 'Cliente eliminado correctamente'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)#error en el servidor
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=403)
#get_object_or_404 devueove un objeto o genra una excepcion
    
from django.shortcuts import render #funciones de django
from .forms import ServicioForm #traer el formulario de servicio de la app
from django.contrib import messages#se utiliza para mostrar mensajes
from .models import Servicio #importa el modelo de servicio de la app
from django.shortcuts import render, get_object_or_404, redirect  #indica que va a recuperar un argumento y va a devolver un httpresponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def create_servicio(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST)  # Vincula el formulario con los datos POST
        if form.is_valid():
            form.save() # Guarda los datos en la base de datos
            messages.success(request, 'Servicio creado con exito.') # Muestra un mensaje de éxito
            return redirect('listar_servicio') # Redirige a la página de listado de los servicio
        else:
            messages.error(request, 'Error al insertar datos. Revise los datos.')
            messages.error(request, form.errors)  # Agrega mensajes de error detallados
    else:
        form = ServicioForm()  # Crea un objeto vacío 
    return render(request, 'control-ajuste.html', {'form': form})# Renderiza la plantilla HTML con el formulario

#funcion para mostrar la lista de los servicios
def listar_servicio(request): #hacemos la solicitud al servidor con la funcion request
    servicios = Servicio.objects.all() #mostramos los servicio almacenaso en la base de datos
    return render (request, "control-ajuste.html", {"servicios":servicios}) #respuesta del servidor en la pagina control-ajuste

#funcion para actualizar o modificar los datos del servicio
def update_servicio(request, id_servicio): #obtener los datos del servicio mediante el id
    servicio = get_object_or_404(Servicio, id_servicio=id_servicio)
    if request.method == 'POST': #revisa si la solicitud es post y puede enviar los nuevos datos
        form = ServicioForm(request.POST, instance=servicio) #se crea el formulario para la validacion
        if form.is_valid():
            form.save()#si son validos se guardan 
            data = {'message': 'Datos actualizados correctamente'} 
            return redirect('listar_servicio') #se regresa al la pagina donde estan los servicios
        else:
            data = {'error': 'Error al actualizar datos. Revise los datos.'}
            return JsonResponse(data)
    else:
        data = {
            'nombre_servicio':servicio.nombre_servicio,
        }
        
        return JsonResponse(data)#toma los datos almacenado y los envia  a donde se ralizo la solicitud

@csrf_exempt # desactiva la protección CSRF para que se pueda eliminar registros
def delete_servicio(request, id_servicio):
    if request.method == 'POST':
        try:
            servicio = get_object_or_404(Servicio, id_servicio=id_servicio) 
            servicio.delete()
            return JsonResponse({'message': 'Servicio eliminado correctamente'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)#error en el servidor
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=403)
#get_object_or_404 devueove un objeto o genra una excepcion
    
    from django.shortcuts import render #funciones de django
from .forms import EquipoForm #traer el formulario de Equipo de la app
from django.contrib import messages#se utiliza para mostrar mensajes
from .models import Equipo #importa el modelo de Equipo de la app
from django.shortcuts import render, get_object_or_404, redirect  #indica que va a recuperar un argumento y va a devolver un httpresponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def create_equipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST)  # Vincula el formulario con los datos POST
        if form.is_valid():
            form.save() # Guarda los datos en la base de datos
            messages.success(request, 'Soporte creado con exito.') # Muestra un mensaje de éxito
            return redirect('listar_soporte') # Redirige a la página de listado de los servicio
        else:
            messages.error(request, 'Error al insertar datos. Revise los datos.')
            messages.error(request, form.errors)  # Agrega mensajes de error detallados
    else:
        form = EquipoForm()  # Crea un objeto vacío 
    return render(request, 'control_soporte.html', {'form': form})# Renderiza la plantilla HTML con el formulario

#funcion para mostrar la lista de los servicios
def listar_equipo(request): #hacemos la solicitud al servidor con la funcion request
    Equipos = Equipo.objects.all() #mostramos los servicio almacenaso en la base de datos
    return render (request, "control_soporte.html", {"equipos":Equipos}) #respuesta del servidor en la pagina control-ajuste

#funcion para actualizar o modificar los datos del servicio
def update_equipo(request, id_equipo): #obtener los datos del equipo mediante el id
    equipo = get_object_or_404(Equipo, id_equipo=id_equipo)
    if request.method == 'POST': #revisa si la solicitud es post y puede enviar los nuevos datos
        form = EquipoForm(request.POST, instance=equipo) #se crea el formulario para la validacion
        if form.is_valid():
            form.save()#si son validos se guardan 
            data = {'message': 'Datos actualizados correctamente'} 
            return redirect('listar_equipo') #se regresa al la pagina donde estan los servicios
        else:
            data = {'error': 'Error al actualizar datos. Revise los datos.'}
            return JsonResponse(data)
    else:
        data = {
            'nombre_equipo':equipo.nombre_equipo,
        }
        
        return JsonResponse(data)#toma los datos almacenado y los envia  a donde se ralizo la solicitud

@csrf_exempt # desactiva la protección CSRF para que se pueda eliminar registros
def delete_equipo(request, id_equipo):
    if request.method == 'POST':
        try:
            equipo = get_object_or_404(Equipo, id_equipo=id_equipo) 
            equipo.delete()
            return JsonResponse({'message': 'Equipo eliminado correctamente'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)#error en el servidor
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=403)
#get_object_or_404 devueove un objeto o genra una excepcion
from django.urls import path
from django.contrib.auth.decorators import login_required #que sea necesario iniciar sesion


#vistas
from . import views
urlpatterns = [
#  CRUD cliente
    path('create',views.create_cliente, name='create'),
    path('listar', login_required (views.listar_cliente), name='listar'),
    path('editar_cliente/<int:id_cliente>', login_required (views.update_cliente), name='editar_cliente'),
    path('eliminar/<int:id_cliente>', views.delete_cliente, name='eliminar_cliente'),
#  CRUD servicio
    path('create_servicio',views.create_servicio, name='create_servicio'),
    path('listar_servicio', login_required (views.listar_servicio), name='listar_servicio'),
    path('editar_servicio/<int:id_servicio>', login_required (views.update_servicio), name='editar_servicio'),
    path('eliminar/<int:id_servicio>', views.delete_servicio, name='eliminar_servicio'),

#   CRUD Equipo
    path('create_equipo',views.create_equipo, name='create_equipo'),
    path('listar_equipo', login_required (views.listar_equipo), name='listar_equipo'),
    path('editar_equipo/<int:id_equipo>', login_required (views.update_equipo), name='editar_equipo'),
    path('eliminar/<int:id_equipo>', views.delete_equipo, name='eliminar_equipo'),

    path('',views.inicioAdmin, name='inicioAdmin'),
    path('control_clientes/',views.control_clientes, name= 'control_clientes'),
    path('control_contratos/',views.control_contratos, name= 'control_contratos'),
    path('control_soporte/',views.control_soporte, name= 'control_soporte'),
    path('control_pagos/',views.control_pagos, name= 'control_pagos'),
    path('control_ajuste/',views.control_ajuste, name= 'control_ajuste'),
    path('equipo_cliente/',views.equipo_cliente, name= 'equipo_cliente'),
    path('tickets_cliente/',views.tickets_cliente, name= 'tickets_cliente'),
    path('contratos_cliente/',views.contratos_cliente, name= 'contratos_cliente'),
    path('pagos_cliente/',views.pagos_cliente, name= 'pagos_cliente'),
    path('control_staff/',views.control_staff, name= 'control_staff'),
]


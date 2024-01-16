from django.urls import path
from .views import control_clientes, control_contratos, control_soporte, control_ajuste, equipo_cliente,tickets_cliente,contratos_cliente,pagos_cliente


#vistas
from . import views
urlpatterns = [
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

]


from django.urls import path
from .views import control_clientes, control_contratos, control_soporte


#vistas
from . import views
urlpatterns = [
    path('',views.inicioAdmin, name='inicioAdmin'),
    path('control_clientes/',views.control_clientes, name= 'control_clientes'),
    path('control_contratos/',views.control_contratos, name= 'control_contratos'),
    path('control_soporte/',views.control_soporte, name= 'control_soporte'),
    path('control_pagos/',views.control_pagos, name= 'control_pagos'),
]

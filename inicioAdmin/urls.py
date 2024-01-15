from django.urls import path
from .views import control_clientes, control_contratos


#vistas
from . import views
urlpatterns = [
    path('',views.inicioAdmin, name='inicioAdmin'),
    path('control_clientes/',views.control_clientes, name= 'control_clientes'),
    path('control_contratos/',views.control_contratos, name= 'control_contratos'),
]
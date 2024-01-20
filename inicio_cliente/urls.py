from django.urls import path
from .views import contratos_cliente,equipo_cliente,tickets_cliente,pagos_cliente
#vistas
from . import views
urlpatterns = [
    path('',views.inicio_cliente, name='inicio_cliente'),
    path('equipo_cliente/',views.equipo_cliente, name= 'equipo_cliente'),
    path('tickets_cliente/',views.tickets_cliente, name= 'tickets_cliente'),
    path('contratos_cliente/',views.contratos_cliente, name= 'contratos_cliente'),
    path('pagos_cliente/',views.pagos_cliente, name= 'pagos_cliente'),
]
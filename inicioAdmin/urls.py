from django.urls import path
from .views import control_clientes


#vistas
from . import views
urlpatterns = [
    path('',views.inicioAdmin, name='inicioAdmin'),
    path('control_clientes/',views.control_clientes, name= 'control_clientes'),
]
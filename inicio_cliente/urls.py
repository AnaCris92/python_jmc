from django.urls import path

#vistas
from . import views
urlpatterns = [
    path('inicio_cliente',views.inicio_cliente, name='inicio_cliente'),
  
]
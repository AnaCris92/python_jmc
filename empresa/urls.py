from django.urls import path
from .views import index, empresa, mantenimiento, sWeb, menuAspel

#vistas
from . import views
urlpatterns = [
    path('',views.empresa, name='empresa'),
    path('indes/', index, name='index'),
    path('mantenimiento/', mantenimiento, name='mantenimiento'),
    path('sWeb/', sWeb, name='sWeb'),
    path('menuAspel/', sWeb, name='menuAspel'),
]
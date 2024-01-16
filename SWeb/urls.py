from django.urls import path
from .views import empresa, mantenimiento, menuAspel

#vistas
from . import views
urlpatterns = [
    path('',views.sWeb, name='sWeb'),
    path('empresa/', empresa, name='empresa'),
    path('mantenimiento/', mantenimiento, name='mantenimiento'),
    path('menuAspel/', menuAspel, name='menuAspel'),

]
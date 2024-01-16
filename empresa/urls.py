from django.urls import path
from .views import index, login, mantenimiento, sWeb, menuAspel

#vistas
from . import views
urlpatterns = [
    path('',views.empresa, name='empresa'),
    path('index/', index, name='index'),
    path('mantenimiento/', mantenimiento, name='mantenimiento'),
    path('sWeb/', sWeb, name='sWeb'),
    path('menuAspel/', sWeb, name='menuAspel'),
    path('login/', login, name='login'),
]
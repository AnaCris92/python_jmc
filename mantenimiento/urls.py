from django.urls import path
from .views import index, empresa, sWeb, menuAspel, login

#vistas
from . import views
urlpatterns = [
    path('',views.mantenimiento, name='mantenimiento'),
    path('index/', index, name='index'),
    path('empresa/', empresa, name='empresa'),
    path('sWeb/', sWeb, name='sWeb'),
    path('menuAspel/', menuAspel, name='menuAspel'),
    path('login/', login, name='login')
]

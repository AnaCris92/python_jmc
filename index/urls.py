from django.urls import path
from .views import index, empresa, mantenimiento

#vistas
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('', index, name='index'),
    path('empresa/', empresa, name='empresa'),
    path('mantenimiento/', mantenimiento, name='mantenimiento'),
]

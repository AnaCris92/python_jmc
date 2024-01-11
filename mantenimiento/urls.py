from django.urls import path

#vistas
from . import views
urlpatterns = [
    path('',views.mantenimiento, name='mantenimiento')
]
from django.urls import path
from .views import index

#vistas
from . import views
urlpatterns = [
    path('',views.index, name='index'),
  #  path('empresa/', views.empresa, name='empresa'),
  #  path('mantenimiento/',views. mantenimiento, name='mantenimiento'),
  #  path('sWeb/',views. sWeb, name='sWeb'),
  #  path('menuAspel/',views. menuAspel, name='menuAspel'),
  #  path('login/', views.login, name='login'),
]

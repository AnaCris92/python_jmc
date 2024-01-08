from django.urls import path

#vistas
from . import views
urlpatterns = [
    path('',views.index, name='index')
]
from django.urls import path

#vistas
from . import views
urlpatterns = [
    path('',views.login, name='login'),
    
]
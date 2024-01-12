from django.urls import path
from .views import sae

#vistas
from . import views
urlpatterns = [
    path('',views.menuAspel, name= 'menuAspel'),
    path('sae/', sae, name='sae'),
]
from django.urls import path
from .views import sae,coi

#vistas
from . import views
urlpatterns = [
    path('',views.menuAspel, name= 'menuAspel'),
    path('sae/', sae, name='sae'),
    path('coi/', sae, name='coi'),
]
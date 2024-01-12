from django.urls import path
from .views import sae,coi,noi

#vistas
from . import views
urlpatterns = [
    path('',views.menuAspel, name= 'menuAspel'),
    path('sae/', sae, name='sae'),
    path('coi/', coi, name='coi'),
    path('noi/', noi, name='noi'),
]
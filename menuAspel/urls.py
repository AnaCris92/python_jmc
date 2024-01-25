from django.urls import path

#vistas
from . import views

urlpatterns = [
    path('',views.menuAspel, name= 'menuAspel'),
    path('adm/',views.adm, name= 'adm'),
    path('sae/',views.sae, name='sae'),
    path('coi/',views.coi, name='coi'),
    path('noi/',views.noi, name='noi'),
    path('caja/',views.caja, name='caja'),
    path('prod/',views.prod, name='prod'),
    path('facture/',views.facture, name='facture'),
    path('banco/',views.banco, name='banco'),
]

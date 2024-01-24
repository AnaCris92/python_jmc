from django.urls import path
from .views import menuAspel,sae,coi,noi,adm,caja,prod,facture,banco

#vistas
urlpatterns = [
    path('',menuAspel, name= 'menuAspel'),
    path('adm/',adm, name= 'adm'),
    path('sae/',sae, name='sae'),
    path('coi/',coi, name='coi'),
    path('noi/',noi, name='noi'),
    path('caja/',caja, name='caja'),
    path('prod/',prod, name='prod'),
    path('facture/',facture, name='facture'),
    path('banco/',banco, name='banco'),
]

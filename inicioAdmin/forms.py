#forms de cliente
from django import forms
from django.forms import ModelForm
from .models import Cliente,Servicio,Equipo
#forms

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["id_cliente","nombre",  "correo","direccion", "telefono", "rfc","cp","estado","nom_contacto",]
#el formulario va dependiendo los campops del modelo y los formularios usados en los modales
        #nita: respetar el orden para que funcione

# forms de servicio

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ["id_servicio","nombre_servicio","descripcion","costo", "plan",]
#el formulario va dependiendo los campops del modelo y los formularios usados en los modales
        #nita: respetar el orden para que funcione
  # forms de equipo      
class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['tipo_equipo', 'marca', 'ram', 'procesador', 'tipo_disco', 'uso_disco', 'ip_local', 'anydesk', 'nom_usuario', 'nom_antivirus', 'vig_antivirus','office','vig_office','descripcion']

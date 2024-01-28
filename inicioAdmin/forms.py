#forms de cliente
from django import forms
from django.forms import ModelForm
from .models import Cliente,Servicio,Soporte


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
from django import forms
from .models import Soporte

class SoporteForm(forms.ModelForm):
    class Meta:
        model = Soporte
        fields = ['fecha', 'nombre', 'contrato', 'periodo', 'inicio', 'termino', 'rfc', 'servicio', 'nom_contacto', 'mensaje', 'archivo']

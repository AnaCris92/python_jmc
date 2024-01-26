#models.py
from django.db import models
from django.core.validators import RegexValidator

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80)
    correo = models.EmailField(null=True, blank=True)
    direccion = models.CharField(max_length=100, null=True, blank=True)
    telefono = models.CharField(max_length=10, null=True, blank=True)
    rfc = models.CharField(max_length=13, null=True, blank=True)
    cp = models.CharField(max_length=5)
    nom_contacto = models.CharField(max_length=50)

    # Campo de estado con validación
    estado = models.CharField(
        max_length=50,
        validators=[
            RegexValidator(
                regex='^[a-zA-Z]+$',
                message='El estado no puede contener números.',
                code='invalid_estado'
            )
        ],
        null=True,  # Puedes cambiar esto según tus requisitos
        blank=True,
    )


    def __str__(self):
        managed = True

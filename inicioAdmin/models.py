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

    from django.db import models

class Servicio(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    nombre_servicio = models.CharField(max_length=80)
    descripcion = models.CharField(max_length=600, null=True, blank=True)
    costo = models.CharField(max_length=20, null=True, blank=True)
    plan = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        managed = True

class Soporte(models.Model):
    fecha = models.DateField(verbose_name='Fecha del ticket', null=True, blank=True)
    nombre = models.CharField(max_length=80, verbose_name='Nombre del cliente')
    contrato = models.CharField(max_length=80, verbose_name='Contrato')
    periodo = models.CharField(max_length=80, verbose_name='Periodo')
    inicio = models.CharField(max_length=80, verbose_name='Inicio')
    termino = models.CharField(max_length=80, verbose_name='Término')
    rfc = models.CharField(max_length=13, verbose_name='RFC')
    servicio = models.CharField(max_length=13, verbose_name='Servicio')
    nom_contacto = models.CharField(max_length=50, verbose_name='Contacto')
    mensaje = models.CharField(max_length=600, verbose_name='Asunto del ticket')
    archivo = models.FileField(upload_to='ticket_archivos/', verbose_name='Archivo')

    def __str__(self):
        managed = True

    

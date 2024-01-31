#models.py
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

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

class Equipo(models.Model):

    TIPO_EQUIPO_CHOICES = [
        ('ao', 'All in One'),
        ('pc', 'Escritorio'),
        ('lap', 'Laptop'),
    ]

    TIPO_DISCO_CHOICES = [
        ('hdd', 'HDD'),
        ('ssd', 'SSD'),
    ]

    tipo_equipo = models.CharField(max_length=20, choices=TIPO_EQUIPO_CHOICES, default='no')
    marca = models.CharField(max_length=50)
    ram = models.CharField(max_length=10)
    procesador = models.CharField(max_length=50)
    tipo_disco = models.CharField(max_length=3, choices=TIPO_DISCO_CHOICES, default='no')
    uso_disco = models.CharField(max_length=15, blank=True, null=True)
    ip_local = models.CharField(max_length=15)
    anydesk = models.CharField(max_length=12)
    nom_usuario = models.CharField(max_length=50)
    nom_antivirus = models.CharField(max_length=20)
    vig_antivirus = models.DateField()
    office = models.CharField(max_length=30)
    vig_office = models.DateField()
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.tipo_equipo} - {self.marca} - {self.nom_usuario}"

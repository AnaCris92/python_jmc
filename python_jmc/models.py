# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Bitacora(models.Model):
    id_bitacora = models.AutoField(primary_key=True)
    asunto = models.CharField(max_length=180, blank=True, null=True)
    mensaje = models.CharField(max_length=600, blank=True, null=True)
    status_bitacora = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bitacora'


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    correo = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=10, blank=True, null=True)
    rfc = models.CharField(max_length=13, blank=True, null=True)
    rf = models.CharField(max_length=45, blank=True, null=True)
    cp = models.CharField(max_length=5)
    municipio = models.CharField(max_length=50, blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)
    nom_contacto = models.CharField(max_length=50)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'


class Contrato(models.Model):
    id_contrato = models.IntegerField(primary_key=True)
    fecha_contrato = models.DateField(blank=True, null=True)
    status_contrato = models.CharField(max_length=20, blank=True, null=True)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    id_servicio = models.ForeignKey('Servicio', models.DO_NOTHING, db_column='id_servicio', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contrato'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Pago(models.Model):
    id_pago = models.AutoField(primary_key=True)
    fecha = models.DateField(blank=True, null=True)
    pdf = models.TextField(blank=True, null=True)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    id_staff = models.ForeignKey('Staff', models.DO_NOTHING, db_column='id_staff', blank=True, null=True)
    id_contrato = models.ForeignKey(Contrato, models.DO_NOTHING, db_column='id_contrato', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pago'


class Servicio(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)
    descripcion = models.CharField(max_length=600, blank=True, null=True)
    costo = models.CharField(max_length=20, blank=True, null=True)
    plan = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servicio'


class Staff(models.Model):
    id_staff = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)
    telefono = models.CharField(max_length=10, blank=True, null=True)
    departamento = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff'


class Ticket(models.Model):
    id_ticket = models.AutoField(primary_key=True)
    mensaje = models.CharField(max_length=600, blank=True, null=True)
    status_ticket = models.CharField(max_length=20, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    prioridad = models.CharField(max_length=20, blank=True, null=True)
    tipo_imagen = models.TextField(blank=True, null=True)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    id_contrato = models.ForeignKey(Contrato, models.DO_NOTHING, db_column='id_contrato', blank=True, null=True)
    id_staff = models.ForeignKey(Staff, models.DO_NOTHING, db_column='id_staff', blank=True, null=True)
    id_bitacora = models.ForeignKey(Bitacora, models.DO_NOTHING, db_column='id_bitacora', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ticket'


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=50)
    password = models.CharField(max_length=12)
    perfil = models.CharField(max_length=20, blank=True, null=True)
    email_rec = models.CharField(max_length=50, blank=True, null=True)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    id_staff = models.ForeignKey(Staff, models.DO_NOTHING, db_column='id_staff', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'

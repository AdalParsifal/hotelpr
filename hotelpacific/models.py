from django.db import models
from django.contrib.auth.models import AbstractUser

# Modelo de Rol
class Rol(models.Model):
    descripcion_rol = models.CharField(max_length=255)

    def __str__(self):
        return self.descripcion_rol

# Modelo de Usuario extendido, con clave foránea hacia Rol
class Usuario(AbstractUser):
    ESTADO_CHOICES = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo')
    ]

    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True)  # Clave foránea a Rol
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)

    def __str__(self):
        return self.username

# Modelo de Habitacion
class Habitacion(models.Model):
    TIPO_CHOICES = [
        ('Individual', 'Individual'),
        ('Doble', 'Doble'),
        ('Suite', 'Suite')
    ]
    ESTADO_CHOICES = [
        ('Disponible', 'Disponible'),
        ('Ocupada', 'Ocupada')
    ]

    tipo_habitacion = models.CharField(max_length=50, choices=TIPO_CHOICES)
    estado_habitacion = models.CharField(max_length=20, choices=ESTADO_CHOICES)
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Habitación {self.tipo_habitacion}'

# Modelo de Reserva
class Reserva(models.Model):
    ESTADO_RESERVA_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('Confirmada', 'Confirmada'),
        ('Cancelada', 'Cancelada')
    ]

    fecha_reserva = models.DateField()
    estado_reserva = models.CharField(max_length=20, choices=ESTADO_RESERVA_CHOICES)
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='reservas')  # Clave foránea a Usuario (cliente)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)  # Clave foránea a Habitacion
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Reserva {self.id} - {self.estado_reserva}'

# Modelo de Turno
class Turno(models.Model):
    fecha_turno = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    trabajador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='turnos_trabajador')  # Clave foránea a Usuario (trabajador)
    supervisor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='turnos_supervisor')  # Clave foránea a Usuario (supervisor)

    def __str__(self):
        return f'Turno {self.id} - Trabajador {self.trabajador.username}'

# Modelo de Pago
class Pago(models.Model):
    fecha_pago = models.DateField()
    monto_pago = models.DecimalField(max_digits=10, decimal_places=2)
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)  # Clave foránea a Reserva
    metodo_pago = models.CharField(max_length=50)

    def __str__(self):
        return f'Pago {self.id} - {self.monto_pago}'

# Modelo de Ticket
class Ticket(models.Model):
    fecha_ticket = models.DateField()
    pago = models.ForeignKey(Pago, on_delete=models.CASCADE)  # Clave foránea a Pago
    codigo_ticket = models.CharField(max_length=50)

    def __str__(self):
        return f'Ticket {self.codigo_ticket}'

# Modelo de Permiso
class Permiso(models.Model):
    descripcion_permiso = models.CharField(max_length=255)

    def __str__(self):
        return self.descripcion_permiso

# Modelo intermedio de Rol y Permiso
class RolPermiso(models.Model):
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)  # Clave foránea a Rol
    permiso = models.ForeignKey(Permiso, on_delete=models.CASCADE)  # Clave foránea a Permiso

    def __str__(self):
        return f'{self.rol.descripcion_rol} - {self.permiso.descripcion_permiso}'

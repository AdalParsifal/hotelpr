from django.contrib import admin
from .models import Usuario, Rol, Habitacion, Reserva, Turno, Pago, Ticket, Permiso, RolPermiso

admin.site.register(Usuario)
admin.site.register(Rol)
admin.site.register(Habitacion)
admin.site.register(Reserva)
admin.site.register(Turno)
admin.site.register(Pago)
admin.site.register(Ticket)
admin.site.register(Permiso)
admin.site.register(RolPermiso)
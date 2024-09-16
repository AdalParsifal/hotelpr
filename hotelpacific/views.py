from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm
from .models import Usuario
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.utils.crypto import get_random_string


def home(request):
    return render (request, 'home.html')
def recovery(request):
    return render (request, 'recovery.html')
def menu_u(request):
    return render(request, 'menu_u.html')
def reservar(request):
    return render(request, 'reservar.html')

def ver_hab(request, id):
    context = {'habitacion_id': id}
    return render(request, 'ver_hab.html', context)
def disponibilidad_habitaciones(request):
    # recuperar habitaciones disponibles desde bd
    habitaciones_disponibles = ['Habitación 1', 'Habitación 2', 'Habitación 3']
    context = {'habitaciones': habitaciones_disponibles}
    return render(request, 'disponibilidad.html', context)
def consultar_reserva(request):
    return render(request, 'consultar_reserva.html')

# Inicio de sesión para usuarios
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            # Mensaje de error si la autenticación falla
            return render(request, 'login_user.html', {'error': 'Credenciales incorrectas'})
    return render(request, 'login_user.html')

# Inicio de sesión para admins/trabajadores
def login_admin(request):
    if request.method == 'POST':
        username = request.POST['admin_username']
        password = request.POST['admin_password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            return render(request, 'login_admin.html', {'error': 'Acceso no autorizado o credenciales incorrectas'})
    return render(request, 'login_admin.html')

# Registro de usuarios
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.rol = 'Cliente'
            user.save()
            return redirect('login_user')
    else:
        form = CustomUserCreationForm()
    return render(request, 'home.html', {'form': form})

temp_codes = {}

def recovery_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        # Lógica para enviar código
        temp_codes[email] = ()
        messages.success(request, 'Código enviado a tu correo.')
        return redirect('confirm_code')
    return render(request, 'recovery_password.html')

def confirm_code(request):
    if request.method == 'POST':
        email = request.POST['email']
        code = request.POST['codigo']
        if temp_codes.get(email) == code:
            messages.success(request, 'Código confirmado, puedes crear una nueva contraseña.')
            return redirect('set_new_password', email=email)
        else:
            messages.error(request, 'El código es incorrecto.')
    return render(request, 'confirm_code.html')

def set_new_password(request, email):
    if request.method == 'POST':
        password1 = request.POST['new_password']
        password2 = request.POST['confirm_password']
        if password1 == password2:
            try:
                user = User.objects.get(email=email)
                user.set_password(password1)
                user.save()
                messages.success(request, 'Tu contraseña ha sido actualizada con éxito.')
                return redirect('login')
            except User.DoesNotExist:
                messages.error(request, 'Ha ocurrido un error, usuario no encontrado.')
        else:
            messages.error(request, 'Las contraseñas no coinciden.')
    return render(request, 'set_new_password.html')

def password_reset_success(request):
    return render(request, 'home.html')
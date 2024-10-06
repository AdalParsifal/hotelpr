from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm
from .forms import UserForm
from .models import Usuario
from .models import Rol
from .models import Habitacion
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
def admin_menu(request):
    return render(request, 'admin_menu.html')

def ver_hab(request):
    habitaciones = Habitacion.objects.all()  # Obtener todas las habitaciones
    context = {
        'habitaciones': habitaciones,
    }
    return render(request, 'ver_hab.html', context)
def disponibilidad_habitaciones(request):
    # recuperar habitaciones disponibles desde bd
    habitaciones_disponibles = ['Habitación 1', 'Habitación 2', 'Habitación 3']
    context = {'habitaciones': habitaciones_disponibles}
    return render(request, 'disponibilidad.html', context)
def pago(request):
    return render(request, 'pago.html')
def confirmar_pago(request):
    if request.method == 'POST':
        return render(request, 'confirmar_pago.html')
    return render(request, 'pago.html')
def reservar(request):
    #exito de reserva, hijo del anterior
    return render(request, 'reservar.html')

def consultar_reserva(request):
    return render(request, 'consultar_reserva.html')
def modificar_reserva(request):
    if request.method == 'POST':
        return redirect('menu')
    return render(request, 'modificar_reserva.html')
def cancelar_reserva(request):
    if request.method == 'POST':
        return redirect('menu')
    return render(request, 'cancelar_reserva.html')
def contacto(request):
    context = {
        'email': 'info@pacificreefhotel.com',
        'telefono': '+123 456 789',
        'direccion': '123 Ocean View, Pacific Reef City'
    }
    return render(request, 'contacto.html', context)

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_menu')
    else:
        form = UserForm()
    return render(request, 'create_user.html', {'form': form})
def edit_user(request, id=None):
    users = Usuario.objects.all()  
    user = None
    form = None

    if id:
        user = get_object_or_404(Usuario, id=id)  
        if request.method == 'POST':
            form = UserForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                return redirect('edit_user')  
        else:
            form = UserForm(instance=user)

    context = {
        'users': users,
        'form': form,
        'user': user
    }
    return render(request, 'edit_user.html', context)
def del_user(request):
    usuarios = Usuario.objects.all()  

    if request.method == 'POST':
        user_id = request.POST.get('user_id') 
        usuario = get_object_or_404(Usuario, id=user_id)  
        usuario.delete()  
        messages.success(request, f'El usuario "{usuario.username}" ha sido eliminado exitosamente.')
        return redirect('del_user') 

    context = {
        'usuarios': usuarios
    }
    return render(request, 'del_user.html', context)


# Inicio de sesión para usuarios
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('menu_u')
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
            return redirect('admin_menu')
        else:
            return render(request, 'login_admin.html', {'error': 'Acceso no autorizado o credenciales incorrectas'})
    return render(request, 'login_admin.html')

# Registro de usuarios
def register(request):
    if request.method == 'POST':
        print(request.POST.get('username'))  # Verifica si el username está llegando
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            cliente_rol = Rol.objects.get(descripcion_rol='Cliente')
            user.rol = cliente_rol
            user.save()
            messages.success(request, 'Registro completado con éxito. ¡Bienvenido!')
            return render(request, 'home.html', {'form': form})
        else:
            print(f"Errores del formulario: {form.errors}")
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
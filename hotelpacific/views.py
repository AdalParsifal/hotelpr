from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm

def home(request):
    return render (request, 'home.html')
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
            form.save()
            return redirect('login_user')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})
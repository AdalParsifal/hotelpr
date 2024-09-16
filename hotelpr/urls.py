"""
URL configuration for hotelpr project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hotelpacific import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('home/', views.home, name='home'),
    path('login_user/', views.login_user, name='login_user'),
    path('login_admin/', views.login_admin, name='login_admin'),
    path('register/', views.register, name='register'),
    
    path('recovery_password/', views.recovery_password, name='recovery_password'),
    path('confirm_code/', views.confirm_code, name='confirm_code'),
    path('set_new_password/<str:email>/', views.set_new_password, name='set_new_password'),

    path('menu_u/', views.menu_u, name='menu_u'),
    path('habitacion/<int:id>/', views.ver_hab, name='ver_hab'),
    path('disponibilidad/', views.disponibilidad_habitaciones, name='disponibilidad'),
    path('pago/', views.pago, name='pago'),
    path('confirmar_pago/', views.confirmar_pago, name='confirmar_pago'),
    path('reservar/', views.reservar, name='reservar'),
    
    path('consultar_reserva/', views.consultar_reserva, name='consultar_reserva'),
    path('modificar_reserva/', views.modificar_reserva, name='modificar_reserva'),
    path('cancelar_reserva/', views.cancelar_reserva, name='cancelar_reserva'),
    path('contacto/', views.contacto, name='contacto'),

    path('admin_menu/', views.admin_menu, name='admin_menu'),
]

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
    
]

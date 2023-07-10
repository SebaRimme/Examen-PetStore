from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.models import User
from .forms import FormularioSesion, RegistroUsuario
from sweetify import info, success, warning, error

# Create your views here.

def mostrar_sesion(request):
    if request.method == 'GET':
        contexto = {
            'titulo': 'Bienvenido',
            'formulario': FormularioSesion(),
        }
        return render(request, 'sesion.html', contexto)
    if request.method == 'POST':
        datos_usuario = FormularioSesion(data = request.POST)
        es_valido = datos_usuario.is_valid()
        if es_valido:
            usuario = authenticate(
                username = datos_usuario.cleaned_data['nombre_usuario'],
                password = datos_usuario.cleaned_data['contrasenia_usuario']
            )
        if usuario is not None:
            login(request, usuario)
            success(request, f'Bienvenido {usuario.username}')
            return redirect('principal')
        warning(request, 'Usuario y contraseña invalidos')
        contexto = {
            'formulario': datos_usuario
        }
        return render(request, 'sesion.html', contexto)

def mostrar_registro(request):
    if request.method == 'GET':
        contexto = {
            'formulario': RegistroUsuario()
        }
        return render(request, 'registro.html', contexto)
    if request.method == 'POST':
        formulario_registro = RegistroUsuario(data=request.POST)
        es_valido = formulario_registro.is_valid()
        if es_valido:
            usuario_nuevo = formulario_registro.save()
            success(request,'Gracias por registrarse en GamerStore')
            return redirect('sesion')
        contexto = {
            'formulario': formulario_registro
        }
        warning(request,'Los campos estan mal completados, favor de revisarlos')
        return render(request,'registro.html',contexto)
        
def cerrar_sesion(request):
    if request.user.is_authenticated:
        logout(request)
        success(request, 'Sesion cerrada')
    return redirect('principal')



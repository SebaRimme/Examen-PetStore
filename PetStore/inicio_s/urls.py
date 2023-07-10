from django.urls import path
from .views import mostrar_sesion, mostrar_registro, cerrar_sesion

urlpatterns = [
    path('sesion/', mostrar_sesion, name="sesion"),
    path('registro/', mostrar_registro, name="registro"),
    path('salir/', cerrar_sesion, name='salir'),
]
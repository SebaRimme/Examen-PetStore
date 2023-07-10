from django.urls import path
from .views import mostrar_principal, mostrar_pago, guardar_producto, listar_productos, modificar_producto, eliminar_producto

urlpatterns = [
    path('', mostrar_principal, name="principal"),
    path('pago/', mostrar_pago, name="pago"),
    path('guardar/', guardar_producto, name="guardar"),
    path('listar/', listar_productos, name="listar"),
    path('modificar/<id>/', modificar_producto, name="modificar"),
    path('eliminar/<id>/', eliminar_producto, name="eliminar"),
]
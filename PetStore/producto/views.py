from django.shortcuts import render, redirect, get_object_or_404
from producto.models import Producto
from producto.Carrito import Carrito
from .forms import ProductoForm
from sweetify import info, success, warning, error

# Create your views here.

def mostrar_principal(request):

    productos = Producto.objects.all()
    contexto = {
        'productos': productos
    }
    return render(request, 'principal/principal.html', contexto)

def mostrar_pago(request):

    productos = Producto.objects.all()
    contexto = {
        'productos': productos
    }
    return render(request, 'pago/pago.html', contexto)

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("principal")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("principal")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("principal")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("principal")

def guardar_producto(request):

    contexto = {
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            success(request, 'Guardado')
            return redirect('principal')
        else:
            data["form"] = formulario

    return render(request, 'admin/agregar.html', contexto)

def listar_productos(request):

    productos = Producto.objects.all()
    contexto = {
        'productos': productos
    }
    return render(request, 'admin/listar.html', contexto)

def modificar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)

    contexto = {
        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            success(request, 'Modificado correctamente')
            return redirect(to="listar")
        data["form"] = formulario

    return render(request, 'admin/modificar.html', contexto)

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    success(request, 'Eliminado correctamente')
    return redirect(to="listar")
import django
from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib import messages
from .forms import *
from .models import Producto, Categoria
from .forms import FormProducto, RegistroForm
from django.shortcuts import get_list_or_404
from django.db.models import Q

# Create your views here.
def home(request):
    productos = Producto.objects.all().order_by("id")[0:3]
    productos_secundarios = Producto.objects.all().order_by('-id')[:10]    
    categorias = Categoria.objects.all()
    data = {
        'productos': productos,
        'productos_secundarios': productos_secundarios,
        'menu_categorias': categorias        
    }
    return render(request, 'JAGUARETTEKAA/index.html', data)

def acerca_de(request):
    return render(request, 'JAGUARETTEKAA/acerca_de.html')

def contacto(request):
    return render(request, 'JAGUARETTEKAA/contacto.html')

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, "El Usuario se ha registrado correctamente")         
            return HttpResponseRedirect(reverse('login'))
    else:
        form = RegistroForm()      

    return render(request, 'JAGUARETTEKAA/registro.html', {
        'form': form
    })

def login(request):
    return render(request, 'JAGUARETTEKAA/login.html')

def logout(request):
    return render(request, 'JAGUARETTEKAA/logout.html')

def productos(request):
    galeria_productos = Producto.objects.all()
    data = {
        'galeria_productos': galeria_productos,              
    }

    return render(request, 'JAGUARETTEKAA/productos.html', data)

def detalle_producto(request):  
    return render(request, 'JAGUARETTEKAA/detalle_producto.html')

@permission_required('jaguarettekaa.add_producto')
def agregar_producto(request):    
    data = {
        'form': FormProducto()
    }
    if request.method == "POST":
       #user = User.objects.get(username=request.user)
       form = FormProducto(data=request.POST, files=request.FILES)
       if form.is_valid():            
            form.save()
            messages.success(request, "El Producto se ha agregado correctamente")           
       else:
           data["form"] = form
    return render(request, 'JAGUARETTEKAA/agregar_producto.html', data)
    
def buscar_producto(request): 
    productos = Producto.objects.all()
    
    if request.method == "POST":
        buscar = request.POST['buscar']
        lista_productos = Producto.objects.filter(
            Q(titulo__icontains=buscar) | 
            Q(descripcion__icontains=buscar)
        )
        return render(request, 'JAGUARETTEKAA/busqueda.html',{
            'productos': productos,
            'buscar': buscar,
            'lista_productos': lista_productos
        })
    else: 
        return render(request, 'JAGUARETTEKAA/busqueda.html', {
            "productos": productos
        })

@permission_required('jaguarettekaa.change_producto')
def modificar_producto(request, producto_id): 
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == "POST":  
        #user = User.objects.get(username=request.user)   
        #un_articulo.publicador = user
        form = FormProducto(data=request.POST, files=request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, "El Producto se ha actualizado correctamente")
            return redirect(to="index")
    else:
        form = FormProducto(instance = producto)
        return render(request, 'jaguarettekaa/modificar_producto.html', {
            "producto": producto,
            "form": form
        })

@permission_required('jaguarettekaa.delete_producto')
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto.delete()
    messages.success(request, "El Producto se ha eliminado correctamente")
    return redirect(to="index")

@permission_required('jaguarettekaa.add_carrito')
@login_required
def carrito(request):
    return render(request, 'JAGUARETTEKAA/carrito.html')  



    
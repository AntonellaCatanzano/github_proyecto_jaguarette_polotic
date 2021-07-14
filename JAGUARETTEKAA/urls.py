from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import home, contacto, acerca_de, productos, agregar_producto, buscar_producto, modificar_producto, eliminar_producto, carrito, detalle_producto, registro

#Importamos una función llamada "home"
#En este archivo definimos las rutas
urlpatterns = [
    path('', home , name="index"),
    path('acerca_de/', acerca_de , name="acerca_de"),
    path('contacto/', contacto , name="contacto"),
    path('productos/', productos , name="productos"),
    path('agregar_producto/', login_required(agregar_producto) , name="agregar_producto"),
    path('busqueda_producto/', buscar_producto , name="buscar_producto"),
    path('modificar_producto/<int:producto_id>/', login_required(modificar_producto) , name="modificar_producto"),
    path('eliminar_producto/<int:producto_id>/', login_required(eliminar_producto) , name="eliminar_producto"),
    path('detalle_producto/', detalle_producto , name="detalle_producto"),
    path('carrito/', login_required(carrito) , name="carrito"),
     path('registro/', registro , name="registro"),     
]

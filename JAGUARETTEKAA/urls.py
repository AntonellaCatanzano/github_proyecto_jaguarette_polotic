from django.urls import path
from .views import home, contacto, acerca_de, productos, login, agregar_producto, buscar_producto, modificar_producto, eliminar_producto, carrito

#Importamos una función llamada "home"
#En este archivo definimos las rutas
urlpatterns = [
    path('', home , name="index"),
    path('acerca_de/', acerca_de , name="acerca_de"),
    path('contacto/', contacto , name="contacto"),
    path('productos/', productos , name="productos"),
    path('agregar_producto/', agregar_producto , name="agregar_producto"),
    path('busqueda_producto/', buscar_producto , name="buscar_producto"),
    path('modificar_producto/<int:producto_id>/', modificar_producto , name="modificar_producto"),
    path('eliminar_producto/<int:producto_id>/', eliminar_producto , name="eliminar_producto"),
    path('carrito/', carrito , name="carrito"),
]

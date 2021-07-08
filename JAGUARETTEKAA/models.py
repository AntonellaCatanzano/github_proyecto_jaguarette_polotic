from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    descripcion = models.CharField(max_length=64, null=False)

    def __str__(self):
        return self.descripcion

class Producto(models.Model):
    titulo = models.CharField(max_length=64, null= False)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    descripcion = models.TextField(null=False)
    precio = models.IntegerField(null=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="categoria")
    

    def __str__(self):
        return self.titulo

class Carrito(models.Model):
    usuario: models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario")
    productos: models.ManyToManyField(Producto)
    cantidad: models.IntegerField()
    total: models.IntegerField()

    def __str__(self):
        return self.usuario
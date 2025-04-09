from django.db import models

# Modelo Categoría
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

# Modelo Proveedor
class Proveedor(models.Model):
    nombre = models.CharField(max_length=200)
    contacto = models.CharField(max_length=100)
    direccion = models.TextField()

    def __str__(self):
        return self.nombre

# Modelo Producto
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    cantidad = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

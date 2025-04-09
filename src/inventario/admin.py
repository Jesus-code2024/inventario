from django.contrib import admin
from .models import Producto, Categoria, Proveedor

admin.site.register(Categoria)
admin.site.register(Proveedor)
admin.site.register(Producto)

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Producto

# Vista para listar productos
class ProductoListView(ListView):
    model = Producto
    template_name = 'inventario/producto_list.html'
    context_object_name = 'productos'

# Vista para ver detalles de un producto
class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'inventario/producto_detail.html'
    context_object_name = 'producto'

# Vista para crear un nuevo producto
class ProductoCreateView(CreateView):
    model = Producto
    template_name = 'inventario/producto_form.html'
    fields = ['nombre', 'descripcion', 'cantidad', 'precio', 'categoria', 'proveedor']
    success_url = reverse_lazy('producto-list')

# Vista para actualizar un producto
class ProductoUpdateView(UpdateView):
    model = Producto
    template_name = 'inventario/producto_form.html'
    fields = ['nombre', 'descripcion', 'cantidad', 'precio', 'categoria', 'proveedor']
    success_url = reverse_lazy('producto-list')

# Vista para eliminar un producto
class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'inventario/producto_confirm_delete.html'
    success_url = reverse_lazy('producto-list')

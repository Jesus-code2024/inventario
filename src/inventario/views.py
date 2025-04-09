from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Producto
from django.urls import reverse_lazy

class ProductoListView(ListView):
    model = Producto
    template_name = 'inventario/producto_list.html' # La plantilla se encuentra en inventario/templates/inventario/
    context_object_name = 'productos'  # Esto se utilizará en la plantilla para referirse a los productos

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'inventario/producto_detail.html'
    context_object_name = 'producto'

class ProductoCreateView(CreateView):
    model = Producto
    template_name = 'inventario/producto_form.html'
    fields = ['nombre', 'descripcion', 'cantidad', 'precio', 'categoria', 'proveedor']
    success_url = reverse_lazy('producto-list')

class ProductoUpdateView(UpdateView):
    model = Producto
    template_name = 'inventario/producto_form.html'
    fields = ['nombre', 'descripcion', 'cantidad', 'precio', 'categoria', 'proveedor']
    success_url = reverse_lazy('producto-list')

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'inventario/producto_confirm_delete.html'
    success_url = reverse_lazy('producto-list')

from django.shortcuts import render


# Create your views here.

from django.views.generic import(
    ListView,
    DeleteView,
    CreateView,
    TemplateView,
    UpdateView,
    DetailView,
)

from .models import datoProducto
from .forms import DatoProductoForm
from django.urls import reverse_lazy


class Inicio(TemplateView):
    template_name = "inicio.html"



class DatosProductosListView(ListView):
    model= datoProducto
    template_name= "datoProducto/lista.html"
    ordering= 'nombre'
    paginate_by= 3
    context_object_name= 'datoProductos'


class BuscarProductoListView(ListView):
    model = datoProducto
    template_name = "datoProducto/buscar.html"
    context_object_name= 'buscar'

    def get_queryset(self):
        palabra_clave= self.request.GET.get("kword","")
        lista= datoProducto.objects.filter(
            nombre__icontains= palabra_clave
        )
        return lista


class ProductoDetalleListView(DetailView):
    model = datoProducto
    template_name = "datoProducto/detalle.html"
    context_object_name= "detalle"



class datoProductoCreateView(CreateView):
    model = datoProducto
    template_name = "datoProducto/create.html"
    form_class = DatoProductoForm
    success_url= reverse_lazy('datoProducto_app:Lista de productos')

    def form_valid(self, form):
        prod= form.save(commit=False)
        prod.nombre_completo= prod.nombre + ' ' 
        prod.save()
        return super(datoProductoCreateView,self).form_valid(form)


class datoProductoUpdateView(UpdateView):
    model = datoProducto
    template_name = "datoProducto/update.html"
    form_class = DatoProductoForm
    success_url= reverse_lazy('datoProducto_app:Lista de productos')

    def form_valid(self, form):
        prod= form.save(commit=False)
        prod.nombre_completo= prod.nombre + ' ' 
        prod.save()
        return super(datoProductoUpdateView,self).form_valid(form)



class datoProductoDeleteView(DeleteView):
    model = datoProducto
    template_name = "datoProducto/delete.html"
    form_class = DatoProductoForm
    success_url= reverse_lazy('datoProducto_app:Lista de productos')

    def form_valid(self, form):
        prod= form.save(commit=False)
        prod.nombre_completo= prod.nombre + ' ' 
        prod.save()
        return super(datoProductoDeleteView,self).form_valid(form)




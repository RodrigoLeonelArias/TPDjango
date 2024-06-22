from django.contrib import admin
from django.urls import path,re_path,include
from . import views

app_name= 'datoProducto_app'




urlpatterns = [
    path(
        'inicial/',
        views.Inicio.as_view(),
        name='Pagina Inicial'
    ),
    path(
        'lista/',
        views.DatosProductosListView.as_view(),
        name='Lista de productos'
    ),
    path(
        'buscar/',
        views.BuscarProductoListView.as_view(),
        name='Buscar productos'
    ),

    path(
        'detalle/<pk>/',
        views.ProductoDetalleListView.as_view(),
        name='Detalle del producto'
    ),
    
    path(
        'create/',
        views.datoProductoCreateView.as_view(),
        name='Alta de producto'
    ),

    path(
        'update/<pk>',
        views.datoProductoUpdateView.as_view(),
        name='Modificar producto'
    ),

    path(
        'delete/<pk>',
        views.datoProductoDeleteView.as_view(),
        name='Eliminar producto'
    ),
]


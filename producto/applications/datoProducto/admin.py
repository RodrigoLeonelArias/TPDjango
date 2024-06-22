from django.contrib import admin
from .models import datoProducto

# Register your models here.

class datoProductoAdmin(admin.ModelAdmin):
    list_display= (
        'nombre',
        'nombre_completo',
        'precio',
        'stock',
        'Tipo_de_Producto',  
        )

    search_fields= ('nombre',)
    list_filter= ('precio',)




admin.site.register(datoProducto,datoProductoAdmin)

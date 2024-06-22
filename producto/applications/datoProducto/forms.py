from django import forms

from .models import datoProducto

class DatoProductoForm(forms.ModelForm):
    """Form definition for DatoProducto."""

    class Meta:
        """Meta definition for DatoProductoform."""

        model = datoProducto
        fields = (
            'nombre',
            'nombre_completo',
            'precio',
            'stock',
            'Tipo_de_Producto',
            'producto',
            )
        
        

from django.db import models
from applications.tipoProducto.models import tipoProducto

# Create your models here.





class datoProducto(models.Model):
    """Model definition for datoProducto."""

    nombre = models.CharField('Nombre de producto', max_length=50)
    nombre_completo = models.CharField("Nombre completo de producto", max_length=50)
    precio = models.DecimalField('Precio de producto', max_digits=20,decimal_places=2)
    stock = models.DecimalField('Cantidad en stock', max_digits= 20,decimal_places=2)
    Tipo_de_Producto = models.ForeignKey(tipoProducto, on_delete=models.CASCADE)
    producto = models.ImageField('Imagen', upload_to='datoProducto', height_field=None, width_field=None, max_length=None,blank=True)


    class Meta:
        """Meta definition for datoProducto."""

        verbose_name =  'Producto'
        verbose_name_plural =  'Productos'

    def __str__(self):
        """Unicode representation of datoProducto."""
        return self.nombre if self.nombre else ''

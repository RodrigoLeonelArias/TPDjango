from django.db import models


# Create your models here.


class tipoProducto(models.Model):
    """Model definition for tipoProducto."""

    nombre = models.CharField('Nombre', max_length=50)
    descripcion = models.CharField('Descripcion de producto', max_length=50)
    

    class Meta:
        """Meta definition for tipoProducto."""

        verbose_name =  'Tipo de producto'
        verbose_name_plural =  'Tipo de productos'

    def __str__(self):
        """Unicode representation of tipoProducto."""
        return self.nombre 

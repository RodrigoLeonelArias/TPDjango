# Generated by Django 3.2 on 2024-06-13 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datoProducto', '0007_rename_tipoproducto_datoproducto_id_tipoproducto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datoproducto',
            old_name='id_tipoProducto',
            new_name='Tipo_de_Producto',
        ),
    ]

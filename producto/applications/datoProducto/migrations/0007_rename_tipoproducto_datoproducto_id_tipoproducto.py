# Generated by Django 3.2 on 2024-06-13 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datoProducto', '0006_rename_id_tipoproducto_datoproducto_tipoproducto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datoproducto',
            old_name='tipoProducto',
            new_name='id_tipoProducto',
        ),
    ]

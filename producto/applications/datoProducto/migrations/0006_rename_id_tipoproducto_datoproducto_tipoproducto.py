# Generated by Django 3.2 on 2024-06-13 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datoProducto', '0005_auto_20240612_1231'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datoproducto',
            old_name='id_tipoProducto',
            new_name='tipoProducto',
        ),
    ]

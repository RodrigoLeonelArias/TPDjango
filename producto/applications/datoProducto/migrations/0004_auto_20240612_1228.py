# Generated by Django 3.2 on 2024-06-12 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datoProducto', '0003_remove_datoproducto_id_datoproducto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datoproducto',
            name='datosAdicionales',
        ),
        migrations.AlterField(
            model_name='datoproducto',
            name='stock',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Cantidad en stock'),
        ),
        migrations.DeleteModel(
            name='Adicionales',
        ),
    ]

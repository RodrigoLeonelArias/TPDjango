# Generated by Django 3.2 on 2024-06-11 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tipoProducto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipoproducto',
            name='identificacion',
            field=models.CharField(max_length=50, verbose_name='Tipo de producto'),
        ),
    ]

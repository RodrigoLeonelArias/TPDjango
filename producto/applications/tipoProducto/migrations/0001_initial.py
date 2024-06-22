# Generated by Django 3.2 on 2024-06-10 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tipoProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificacion', models.CharField(max_length=50, verbose_name='Id de producto')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('descripcion', models.CharField(max_length=50, verbose_name='Descripcion de producto')),
            ],
            options={
                'verbose_name': 'Tipo de producto',
                'verbose_name_plural': 'Tipo de productos',
            },
        ),
    ]

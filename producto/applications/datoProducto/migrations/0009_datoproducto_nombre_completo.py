# Generated by Django 3.2 on 2024-06-17 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datoProducto', '0008_rename_id_tipoproducto_datoproducto_tipo_de_producto'),
    ]

    operations = [
        migrations.AddField(
            model_name='datoproducto',
            name='nombre_completo',
            field=models.CharField(default='', max_length=50, verbose_name='Nombre completo de producto'),
            preserve_default=False,
        ),
    ]

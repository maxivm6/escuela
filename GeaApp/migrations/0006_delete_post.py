# Generated by Django 4.1.4 on 2023-04-25 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GeaApp', '0005_alter_seccion_color_fondo_alter_seccion_contenido'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]
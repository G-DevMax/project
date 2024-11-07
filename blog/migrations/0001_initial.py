# Generated by Django 4.0 on 2024-11-07 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True # Indica que es la primera migración para la app

    dependencies = [
        # No tiene dependencias, ya que es la primera migración
    ]

    operations = [
        migrations.CreateModel(
            name='Articule', # Se crea el modelo 'Article'
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')), # Campo 'id' autogenerado
                ('title', models.CharField(max_length=225)), # Campo 'title' con longitud máxima de 255 caracteres
                ('content', models.TextField()), # Campo 'content' para texto largo
            ],
        ),
    ] # python manage.py migrate con este comando se aplica las migraciones hechas a la base de datos

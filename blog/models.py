from django.db import models

# Create your models here.

class Article(models.Model): # Definición del modelo "Articulo" (Tabal Articulo)
    title = models.CharField(max_length=225) # cración de la columna "title", que se le asigna con CharField un campo de texto con máximo 225 caracteres, max_length es de caracter obrigatorio 
    content = models.TextField() # cración de la columna "content", que se le asigna con TextField un campo de texto sin limites de caracteres

# python manage.py makemigrations, con este comando se crea un archivo de migración de models.py
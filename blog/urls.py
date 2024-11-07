from django.urls import path
from . import views  # se carga el archivo views.py en el directorio del blog.

urlpatterns = [
    # Se realizan las configuraciones para enviar peticiones a la vista. 
    # En términos simples, esto significa que cuando se hace una petición, se ejecuta la función del index definida en la vista.
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
]
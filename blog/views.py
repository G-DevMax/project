
# Create your views here.
# estas dos lineas son para importar las liberías que necesitaremos usar en una app
from django.shortcuts import render, redirect
# htppResponse se puede intepretar como un contenedor que se enviaría al recibir una petición, es el delivery para el usuario
from .models import Article # Aqui importamos el modelo que creamos
from .forms import ArticleForm

# return HttpResponse("Hello world") # para enviar un Hola Mundo, se usa return y el contenedor donde se devuelve la solicitud de la petición

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = Article(title=form.cleaned_data['title'], content=form.cleaned_data['content'])
            article.save()
            return redirect('index')
    else:
        form = ArticleForm()

    return render(request, 'blog/create.html', {'form': form})

def index(request): # el argumento recibe peticiones y comprueba su contenido
    articles = Article.objects.all()  # Recupera todos los registros del modelo Articule y los asigna a la variable articles.
    params = {  # Crea un diccionario params con los artículos, que se pasará a la plantilla.
        'articles': articles,
    }
    return render(request, 'blog/index.html', params)  # Usa render para combinar la plantilla blog/index.html con los datos y devuelve la respuesta.
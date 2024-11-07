# Aqui se definen los formularios

from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(label='Título', max_length=255)
    content = forms.CharField(label='Contenido', widget=forms.Textarea())
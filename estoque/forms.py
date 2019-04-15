from django.forms import ModelForm
from .models import *
from django.urls import reverse_lazy

class ProdutoForm(ModelForm):
	class Meta:
	    model = Produto
	    fields = ['nome','localizacao','quantidade','categoria']
class CategoriaForm(ModelForm):
	class Meta:
	    model = Categoria
	    fields = ['nome']

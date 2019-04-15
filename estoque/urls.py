from django.contrib import admin
from django.conf.urls import url, include

from views import *
urlpatterns = [
    url(r'^index', home),
    url(r'^produto/(?P<pk>\d+)/$', produto, name='Produto-info'),
    url(r'^venda/(?P<pk>\d+)/$', venda, name='venda'),
	url(r'^produto/add', produto_add, name='Produto-add'),
	url(r'^categoria/add', categoria_add, name='Categoria-add'),
	url(r'^categorias', categorias, name='Categorias'),

    # url('produto/<int:pk>/delete/', ProdutoDelete.as_view(), name='Produto-delete'),

]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from .forms import *

# Create your views here.
# Create your views here.
def home(request):
	produtos = Produto.objects.all()
	return render(request, 'produtos.html',{'produtos':produtos})

def categorias(request):
	categorias = Categoria.objects.all()
	return render(request, 'categorias.html',{'categorias':categorias})

def produto(request, pk):
    produto = get_object_or_404(Produto, id=pk)
    vendas = Venda.objects.filter(produto=produto).order_by('-data')
    return render(request, 'produto.html',{'produto': produto,'vendas':vendas})

def venda(request, pk):
    produto = get_object_or_404(Produto, id=pk)
    venda = Venda(quantidade=1, produto=produto).save()

    return render(request, 'venda.html',{'produto': produto,'pk':pk})

def produto_add(request):
	title = "Cadastrar Produto"
	link = "/produto/add"
	if request.method == 'POST':
		form = ProdutoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/index')
	else:
		form = ProdutoForm()
	return render(request, 'form.html', {'form':form,'title':title,"link":link})

def categoria_add(request):
	title = "Cadastrar Categoria"
	link = "/categoria/add"
	if request.method == 'POST':
		form = CategoriaForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = CategoriaForm()
	return render(request, 'form.html', {'form':form,'title':title,"link":link})


# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime    
# Create your models here.
from django.core.validators import MinValueValidator
# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=1000)
    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=1000, default='')
    localizacao = models.CharField(max_length=1000, default='')
    quantidade = models.IntegerField(validators=[MinValueValidator(1)], default=1)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome

class Venda(models.Model):
    quantidade = models.IntegerField(validators=[MinValueValidator(1)], default=1)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "%s %s" % (self.quantidade, self.produto.nome)
    def save(self, *args, **kwargs):
      
        super(Venda, self).save(*args, **kwargs)
        
        # pega compras relacionadas
        self.produto.quantidade = self.produto.quantidade - self.quantidade
        self.produto.save()
        
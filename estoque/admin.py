# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

admin.site.register(Produto)
admin.site.register(Categoria)
admin.site.register(Venda)
# Register your models here.

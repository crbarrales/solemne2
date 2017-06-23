# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from web.models import Noticias

class NoticiasAdmin(admin.ModelAdmin):
	list_display = ('name','anio','sort_order','id')

admin.site.register(Noticias, NoticiasAdmin)



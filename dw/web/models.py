# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from tinymce import models as tinymce_models

class Noticias(models.Model):
	 name = models.CharField(max_length=144)
	 description = models.TextField()
	 anio = models.PositiveIntegerField()
	 sort_order = models.IntegerField() 
	 
	 
	 

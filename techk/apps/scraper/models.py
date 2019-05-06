# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Categoria(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Libro(models.Model):
    category = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    title = models.CharField(max_length= 300)
    thumbnail = models.URLField(max_length=200)
    price = models.CharField(max_length=8)
    stock = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    upc = models.CharField(max_length=20)

    def __str__(self):
        return self.title
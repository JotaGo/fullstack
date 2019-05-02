# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Libro(models.Model):
    category = models.CharField(max_length=20)
    title = models.CharField(max_length= 100)
    thumbnail = models.URLField(max_length=200)
    price = models.CharField(max_length=8)
    stock = models.CharField(max_length=4)
    product_description = models.TextField()
    upc = models.CharField(max_length=20)

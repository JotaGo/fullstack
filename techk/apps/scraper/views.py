# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from rest_framework import generics
from django.template import loader
from .forms import SearchForm

from .models import Categoria, Libro
from .serializers import CategoriaSerializer, LibroSerializer
from .myscrap import scraper
import pdb

# Create your views here.
def index(request):
    return render(request, 'scraper/base.html')

def execute(request):
    bd = Categoria.objects.all()
    if not bd:
        json = scraper()
        serializer = CategoriaSerializer(data=json[0], many=True)
        if serializer.is_valid():
            serializer.validated_data
            serializer.save()
        serial = LibroSerializer(data=json[1], many=True)
        if serial.is_valid():
            serial.validated_data
            serial.save()
    return redirect('categorias')

def category_list(request):
    categorias = Categoria.objects.all()
    template = loader.get_template('scraper/categorys.html')
    context = {
        'categorias' : categorias
    }
    return HttpResponse(template.render(context,request))

def book_list(request,category_id):
    categoria = Categoria.objects.get(id=category_id)
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            atribute = form.data['Attribute']
            data = form.data['Search']
            if atribute == 'title':
                libros = Libro.objects.filter(category_id=category_id,title__contains=data)
            elif atribute == 'price':
                libros = Libro.objects.filter(category_id=category_id,price__contains=data)
            elif atribute == 'description':
                libros = Libro.objects.filter(category_id=category_id,description__contains=data)
            elif atribute == 'upc':
                libros = Libro.objects.filter(category_id=category_id,upc__contains=data)
            context = {
                'categoria' : categoria,
                'libros' : libros,
                'form' : form,
            }   
            return render(request, 'scraper/books.html', context)
    else:
        form = SearchForm()
    libros = Libro.objects.filter(category_id=category_id)
    context = {
        'categoria' : categoria,
        'libros' : libros,
        'form' : form,
    }
    return render(request, 'scraper/books.html', context)

def book_delete(request,category_id,book_id):
    libro = Libro.objects.get(id=book_id)
    libro.delete()
    return redirect('books', category_id)
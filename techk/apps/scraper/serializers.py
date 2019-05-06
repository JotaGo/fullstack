from .models import Categoria, Libro
from rest_framework import serializers

class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = ('id', 'name')

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = ('id', 'category', 'title', 'thumbnail', 'price', 'stock', 'description', 'upc')
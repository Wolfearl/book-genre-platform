from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publication_year']
        read_only_fields = ['id'] # поля, которые будут игнорироваться при попытках записать или обновить их значение
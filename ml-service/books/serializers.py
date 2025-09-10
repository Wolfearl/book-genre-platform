from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publication_year', 'pages', 'rating']
        read_only_fields = ['id'] # поля, которые будут игнорироваться при попытках записать или обновить их значение
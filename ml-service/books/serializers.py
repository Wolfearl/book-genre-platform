from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model based on Django REST Framework's ModelSerializer.
    Designed to convert Book model data into a transferable format (e.g., JSON) and back.

    Usage example:
        serializer = BookSerializer(book_instance)
        json_data = serializer.data
    """
    class Meta:
        """
        An inner class specifying the model and fields for serialization

        :param model: The model class to be serialized (e.g., Book)
        :type model: Django model class
        :param fields: Fields included in the serialization:
            - id: unique book identifier (read-only)
            - title: book title
            - author: book author
            - publication_year: year of publication
            - pages: number of pages
            - rating: book rating
        :type fields: list of str
        :param read_only_fields: List of fields that are read-only (id)
        :type read_only_fields: list of str
        """
        model = Book
        fields = ['id', 'title', 'author', 'publication_year', 'pages', 'rating']
        read_only_fields = ['id']  # fields that will be ignored when attempting to write or update their value

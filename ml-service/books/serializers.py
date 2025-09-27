from django.core.validators import MinValueValidator, MaxValueValidator
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


class PredictionRequestSerializer(serializers.Serializer):
    """
    Serializer for a book genre prediction query.
    It is used to validate input data when requesting a prediction.

    :param title: book title (required field)
    :type title: str
    :param description: book description (optional, may be empty)
    :type description: str
    :param rating: book rating (optional, number from 0 to 5)
    :type rating: float
    """
    title = serializers.CharField(
        max_length=500,
        required=True,
        help_text="Book title (required field)"
    )
    description = serializers.CharField(
        max_length=5000,
        required=False,
        allow_blank=True,
        default="",
        help_text="Book description (optional)"
    )
    rating = serializers.FloatField(
        required=False,
        default=0.0,
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        help_text="Book rating from 0 to 5 (optional)"
    )


class PredictionResponseSerializer(serializers.Serializer):
    """
    A serializer for the response with the result of predicting the genre of the book.

    :param genre: predicted genre
    :type genre: str
    :param probabilities: a list of the top 3 genres with probabilities, where each element is a list of 2 lines (genre and probability)
    :type probabilities: list[list[str]]
    :param prediction_time: prediction execution time in seconds
    :type prediction_time: float
    :param cached: whether the cache is used
    :type cached: bool
    :param features_used: dictionary of used model features
    :type features_used: dict
    """
    genre = serializers.CharField(help_text="The predicted genre")
    probabilities = serializers.ListField(
        child=serializers.ListField(
            child=serializers.CharField(),
            max_length=2
        ),
        help_text="Top 3 genres with probabilities"
    )
    prediction_time = serializers.FloatField(help_text="Prediction time in seconds")
    cached = serializers.BooleanField(help_text="Is caching used")
    features_used = serializers.DictField(help_text="Used features")


class BatchPredictionRequestSerializer(serializers.Serializer):
    """
    Serializer for batch query of predictions for a list of books.

    :param books: a list of prediction books, each of which is validated by PredictionRequestSerializer
    :type books: list[PredictionRequestSerializer]
    """
    books = serializers.ListField(
        child=PredictionRequestSerializer(),
        help_text="List of books for prediction"
    )


class ModelInfoSerializer(serializers.Serializer):
    """
    Serializer of information about the machine learning model.

    :param status: current model status
    :type status: str
    :param model_type: model type
    :type model_type: str
    :param classes_count: number of classes (genres)
    :type classes_count: int
    :param classes: list of genres that the model works with
    :type classes: list[str]
    """
    status = serializers.CharField(help_text="Model status")
    model_type = serializers.CharField(help_text="Model Type")
    classes_count = serializers.IntegerField(help_text="Number of classes")
    classes = serializers.ListField(child=serializers.CharField(), help_text="List of genres")

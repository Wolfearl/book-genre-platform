import time
from django.db import connection
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from additionally.book_vectors import BookVectorizer
from services.ml_service import ml_service
from services.monitoring import prediction_monitor
from training.predictor import BookGenrePredictor
from django.core.cache import cache

from .serializers import (
    PredictionRequestSerializer,
    PredictionResponseSerializer,
    BatchPredictionRequestSerializer,
    ModelInfoSerializer
)

from .models import Book
from .serializers import BookSerializer

# Create your views here.


@api_view(['GET', 'POST'])
def book_list(request):
    """
    Handles GET and POST requests for working with the book list
    (retrieving all books and adding a new book).

    :param request: HTTP request
    :type request: django.http.HttpRequest
    :return: JSON response with books data or operation status
    :rtype: Response
    """

    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, pk):
    """
    Handles GET, PUT, and DELETE requests to work with a book
    (retrieving, updating and deleting a book by index).

    :param request: HTTP request
    :type request: django.http.HttpRequest
    :param pk: Book index
    :type pk: int
    :return: JSON response with book data or operation status
    :rtype: Response
    """
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def similar_books(request, book_id):
    """
    Processes a GET request to work with a list of books
    (retrieves books similar to the one with the index book_id).

    :param request: HTTP request
    :type request: django.http.HttpRequest
    :param book_id: Book index
    :type book_id: int
    :return: JSON response with books data or operation status
    :rtype: Response
    """
    try:
        target_book = Book.objects.get(pk=book_id)
        all_books = Book.objects.all()

        vectorizer = BookVectorizer()
        similar = vectorizer.find_similar_books(
            {'title': target_book.title, 'pages': target_book.pages,
             'publication_year': target_book.publication_year,
             'rating': target_book.rating},
            [{'title': b.title, 'pages': b.pages, 'publication_year': b.publication_year, 'rating': b.rating}
             for b in all_books if b != target_book]
        )
        # Return the IDs of similar books and their similarity
        result = [{'title': book['title'], 'similarity': similarity} for book, similarity in similar]
        return Response(result)

    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


predictor = BookGenrePredictor()

@api_view(['POST'])
def predict_genre(request):
    """
    Genre prediction for one book.

    :param request: HTTP request
    :type request: django.http.HttpRequest
    :return: JSON response with the book's title and genres
    :rtype: Response
    """
    start_time = time.time()

    # Validation of input data
    serializer = PredictionRequestSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Getting validated data
    data = serializer.validated_data

    # Making a prediction
    try:
        result = ml_service.predict_single(
            title=data['title'],
            description=data.get('description', ''),
            rating=data.get('rating', 0.0),
        )

        prediction_time = time.time() - start_time

        # Recording in monitoring
        if 'error' not in result:
            prediction_monitor.record_prediction(True, prediction_time)
            response_serializer = PredictionResponseSerializer(result)
            return Response(response_serializer.data)
        else:
            prediction_monitor.record_prediction(False, prediction_time)
            return Response(result, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    except Exception as e:
        prediction_time = time.time() - start_time
        prediction_monitor.record_prediction(False, prediction_time)
        return Response(
            {'error': f'Internal server error: {str(e)}'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['GET'])
def health_check(request):
    """
    Checking the health of the service.

    :param request: The HTTP request object passed to the view
    :type request: django.http.HttpRequest
    :return: JSON with the status
    :rtype: Response
    """
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")

        model_info = ml_service.get_model_info()
        return Response({
            'status': 'healthy',
            'database': 'connected',
            'ml_model': model_info['status'],
            'timestamp': time.time()
        })
    except Exception as e:
        return Response({
            'status': 'unhealthy',
            'error': str(e)
        }, status=status.HTTP_503_SERVICE_UNAVAILABLE)


@api_view(['POST'])
def predict_batch(request):
    """
    Batch genre prediction for multiple books.

    :param request: The HTTP request object passed to the view
    :type request: django.http.HttpRequest
    :return: JSON with the results
    :rtype: Response
    """
    start_time = time.time()

    # Validation of input data
    serializer = BatchPredictionRequestSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Performing batch prediction
    try:
        results = ml_service.predict_batch(serializer.validated_data['books'])
        prediction_time = time.time() - start_time

        # Package statistics
        successful = sum(1 for r in results if 'error' not in r)
        failed = len(results) - successful

        # Recording in monitoring
        prediction_monitor.record_prediction(successful > 0, prediction_time)

        return Response({
            'results': results,
            'batch_stats': {
                'total': len(results),
                'successful': successful,
                'failed': failed,
                'processing_time': prediction_time
            }
        })

    except Exception as e:
        prediction_time = time.time() - start_time
        prediction_monitor.record_prediction(False, prediction_time)
        return Response(
            {'error': f'Batch prediction failed: {str(e)}'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['GET'])
def model_info(request):
    """
    Information about the loaded ML model.

    :param request: The HTTP request object passed to the view
    :type request: django.http.HttpRequest
    :return: JSON with the model info
    :rtype: Response
    """
    try:
        m_info = ml_service.get_model_info()
        serializer = ModelInfoSerializer(m_info)
        return Response(serializer.data)
    except Exception as e:
        return Response(
            {'error': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['GET'])
def prediction_stats(request):
    """
    Prediction statistics.

    :param request: The HTTP request object passed to the view
    :type request: django.http.HttpRequest
    :return: JSON with the prediction statistics
    :rtype: Response
    """
    try:
        stats = prediction_monitor.get_stats()
        return Response(stats)
    except Exception as e:
        return Response(
            {'error': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

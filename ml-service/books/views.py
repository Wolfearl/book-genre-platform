from django.core.serializers import serialize
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from book_vectors import BookVectorizer
from .models import Book
from .serializers import BookSerializer


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


@api_view(['GET'])
def predict_genre(request):
    """
    Processes a GET request for working with a book
    (returns the title and genre of the book).

    :param request: HTTP request
    :type request: django.http.HttpRequest
    :return: JSON response with the book's title and genre
    :rtype: Response
    """
    title = request.GET.get('title', '')

    # Here will be the real ML logic; for now, it's a placeholder.
    if 'java' in title.lower() or 'python' in title.lower():
        prediction = 'Programming'
    elif 'любовь' in title.lower():
        prediction = 'Romance'
    else:
        prediction = 'Fiction'

    return Response({'title': title, 'prediction_genre': prediction})

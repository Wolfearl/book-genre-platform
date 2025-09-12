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
    try:
        target_book = Book.objects.get(pk=book_id)
        all_books = Book.objects.all()

        vectorizer = BookVectorizer()
        similar = vectorizer.find_similar_books(
            {'title': target_book.title, 'pages': target_book.pages, 'publication_year': target_book.publication_year,
             'rating': target_book.rating},
            [{'title': b.title, 'pages': b.pages, 'publication_year': b.publication_year, 'rating': b.rating}
             for b in all_books if b != target_book]
        )
        # Возвращаем ID похожих книг и их сходство
        result = [{'title': book['title'], 'similarity': similarity} for book, similarity in similar]
        return Response(result)

    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def predict_genre(request):
    title = request.GET.get('title', '')

    # Здесь будет реальная ML-логика, пока заглушка
    if 'java' in title.lower() or 'python' in title.lower():
        prediction = 'Programming'
    elif 'любовь' in title.lower():
        prediction = 'Romance'
    else:
        prediction = 'Fiction'

    return Response({'title' : title, 'prediction_genre': prediction})
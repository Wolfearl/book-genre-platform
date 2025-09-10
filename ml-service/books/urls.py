from django.urls import path
from . import views


urlpatterns = [
    path('books/similar/<int:book_id>/', views.similar_books, name='similar-books'),
    path('books/<int:pk>/', views.book_detail, name='book-detail'),
    path('books/', views.book_list, name='books-list')
]
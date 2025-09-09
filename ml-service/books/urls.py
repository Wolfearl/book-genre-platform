from django.urls import path
from . import views


urlpatterns = [
    path('books/<int:pk>/', views.book_detail, name='book-detail'),
    path('books/', views.book_list, name='books-list')
]
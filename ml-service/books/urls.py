from django.urls import path
from . import views


urlpatterns = [
    path('books/similar/<int:book_id>/', views.similar_books, name='similar-books'),

    # Basic CRUD endpoints
    path('books/', views.book_list, name='books-list'),
    path('books/<int:pk>/', views.book_detail, name='book-detail'),

    # ML endpoints
    path('predict/batch/', views.predict_batch, name='predict-batch'),
    path('predictions/stats/', views.prediction_stats, name='prediction-stats'),
    path('predict/', views.predict_genre, name='predict-genre'),
    path('model/info/', views.model_info, name='model-info'),

    # System endpoints
    path('health/', views.health_check, name='health-check')
]
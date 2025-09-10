import numpy as np
from typing import List, Dict


class BookVectorizer:
    def __init__(self):
        self.feature_names = ['pages', 'year', 'rating']

    def book_to_vector(self, book_data: Dict) -> np.array:
        """
        Преобразует данные книги в вектор
        book_data: словарь с полями 'pages', 'publication_year', 'rating'
        """
        # Нормализация данных (упрощенная версия)
        pages = book_data.get('pages', 300) / 2000                     # Нормализуем к 0-1
        year = (book_data.get('publication_year', 2000) - 1900) / 150  # Нормализуем
        rating = book_data.get('rating', 3.0) / 5.0                    # Нормализуем к 0-1

        return np.array([pages, year, rating])

    def find_similar_books(self, target_book: Dict, all_books: List[Dict], top_n: int = 20) -> List[Dict]:
        """
        Находит наиболее похожие книги на основе векторного представления
        """
        target_vector = self.book_to_vector(target_book)
        similarities = []
        for book in all_books:
            book_vector = self.book_to_vector(book)

            # Вычисляем косинусное сходство
            dot_product = np.dot(target_vector, book_vector)
            magnitude_target = np.linalg.norm(target_vector)
            magnitude_book = np.linalg.norm(book_vector)
            if magnitude_target > 0 and magnitude_book > 0:
                similarity = dot_product / (magnitude_target * magnitude_book)
                similarities.append((book, similarity))

        # Сортируем по убыванию сходства
        similarities.sort(key=lambda x: x[1], reverse=True)
        if top_n >= len(similarities):
            return similarities[:top_n]
        else:
            return similarities

# Пример использования
if __name__ == "__main__":
    vectorizer = BookVectorizer()

    # Тестовые данные (в реальности будем брать из базы)
    books_data = [
        {'title': 'Book 1', 'pages': 350, 'publication_year': 2001, 'rating': 4.5},
        {'title': 'Book 2', 'pages': 280, 'publication_year': 1998, 'rating': 4.2},
        {'title': 'Book 3', 'pages': 420, 'publication_year': 2010, 'rating': 4.7},
        {'title': 'Book 4', 'pages': 190, 'publication_year': 1985, 'rating': 3.8}
    ]

    target_book = {'title': 'My Book', 'pages': 320, 'publication_year': 2005, 'rating': 4.3}

    similar = vectorizer.find_similar_books(target_book, books_data)
    print("Наиболее похожие книги:")
    for book, similarity in similar:
        print(f"{book['title']}: сходство = {similarity:.3f}")
import numpy as np
from typing import List, Dict


class BookVectorizer:
    """
    Data vectorizer for the book for subsequent comparison.
    """
    def __init__(self):
        """
        Initialization with feature assignment.

        :param self.feature_names: The values by which the comparison is made
        :type self.feature_names: list of str
        """
        self.feature_names = ['pages', 'year', 'rating']

    def book_to_vector(self, book_data: Dict) -> np.array:
        """
        Transforms book data into a vector.
        Normalization of data (simplified version).

        :arg book_data: a dictionary with keys 'pages', 'publication_year', 'rating'
        :type book_data: Dict
        :return: Feature vector for a book (pages, year, rating), normalized
        :rtype: np.array
        """
        pages = book_data.get('pages', 300) / 2000                     # Normalize to 0-1
        year = (book_data.get('publication_year', 2000) - 1900) / 150  # Normalize
        rating = book_data.get('rating', 3.0) / 5.0                    # Normalize to 0-1

        return np.array([pages, year, rating])

    def find_similar_books(self, target_book: Dict, all_books: List[Dict], top_n: int = 3) -> List[Dict]:
        """
        Finds the most similar books based on vector representation

        :arg target_book: Dictionary with book data for comparison
        :type target_book: Dict
        :arg all_books: A list of dictionaries with data of all books
        :type all_books: List[Dict]
        :arg top_n: The number of similar books to return. The default is 3
        :return: List of the most similar books with similarity ratings
        :rtype: List[Dict]
        """
        target_vector = self.book_to_vector(target_book)
        similarities = []
        for book in all_books:
            book_vector = self.book_to_vector(book)

            # Calculating cosine similarity
            dot_product = np.dot(target_vector, book_vector)
            magnitude_target = np.linalg.norm(target_vector)
            magnitude_book = np.linalg.norm(book_vector)
            if magnitude_target > 0 and magnitude_book > 0:
                similarity = dot_product / (magnitude_target * magnitude_book)
                similarities.append((book, similarity))

        # Sort by descending similarity
        similarities.sort(key=lambda x: x[1], reverse=True)
        if top_n >= len(similarities):
            return similarities[:top_n]
        else:
            return similarities


# Usage example
if __name__ == "__main__":
    vectorizer = BookVectorizer()

    # Test data (in reality, we will take it from the database)
    books_data = [
        {'title': 'Book 1', 'pages': 350, 'publication_year': 2001, 'rating': 4.5},
        {'title': 'Book 2', 'pages': 280, 'publication_year': 1998, 'rating': 4.2},
        {'title': 'Book 3', 'pages': 420, 'publication_year': 2010, 'rating': 4.7},
        {'title': 'Book 4', 'pages': 190, 'publication_year': 1985, 'rating': 3.8}
    ]

    target_book = {'title': 'My Book', 'pages': 320, 'publication_year': 2005, 'rating': 4.3}

    similar = vectorizer.find_similar_books(target_book, books_data)
    print("The most similar books:")
    for book, similarity in similar:
        print(f"{book['title']}: similarity = {similarity:.3f}")

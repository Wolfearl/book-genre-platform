from django.db import models

from constants import MAX_BOOK_TITLE_LENGTH, MAX_BOOK_AUTHOR_LENGTH, DEFAULT_BOOK_PAGES, DEFAULT_BOOK_RATING


# Create your models here.


class Book(models.Model):
    """
    Book model that stores information about the title, author, publication year, number of pages, and rating.

    :param title: The book title, with a maximum length of 200 characters
    :type title: str
    :param author: The book author, with a maximum length of 100 characters
    :type author: str
    :param publication_year: The year the book was published
    :type publication_year: int
    :param pages: The number of pages
    :type pages: int
    :param rating: The book rating
    :type rating: float
    """
    title = models.CharField(max_length=MAX_BOOK_TITLE_LENGTH)
    author = models.CharField(max_length=MAX_BOOK_AUTHOR_LENGTH)
    publication_year = models.IntegerField()
    pages = models.IntegerField(default=DEFAULT_BOOK_PAGES)
    rating = models.FloatField(default=DEFAULT_BOOK_RATING)

    def __str__(self):
        """
        Returns a readable string representation of the book.

        :return: The string in the format '"Title" by Author (Publication Year)'
        :rtype: str
        """
        return f'"{self.title}" by {self.author} ({self.publication_year})'

from django.core.management import BaseCommand
from books.models import Book


class Command(BaseCommand):
    """
    Django management command for loading test data into the database.

    :param help: Brief description of the command purpose
    :type help: str
    """
    help = 'Load test data into database'

    def handle(self, *args, **options):
        """
        Executes the command logic:
        - Checks if the Book table is empty
        - If empty, inserts three example Book instances
        - Otherwise informs the user that data already exists

        :param args: Variable length argument list (not used in this command)
        :type args: tuple
        :param options: Arbitrary keyword arguments (not used in this command)
        :type options: dict
        :return: None. Writes a message to stdout about the result of loading test data
        :rtype: None
        """
        if Book.objects.count() == 0:
            Book.objects.create(title="Python Crash Course", author="Eric Matthes", publication_year=2019,
                                pages=544, rating=4)
            Book.objects.create(title="Fluent Python", author="Luciano Ramalho", publication_year=2015,
                                pages=792, rating=4)
            Book.objects.create(title="Deep Learning with Python", author="François Chollet", publication_year=2017,
                                pages=384, rating=3)
            self.stdout.write(self.style.SUCCESS('Successfully loaded test data'))
        else:
            self.stdout.write(self.style.WARNING('Database already contains data'))
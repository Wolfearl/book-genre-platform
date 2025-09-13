from django.apps import AppConfig


class BooksConfig(AppConfig):
    """
    Application configuration class 'books' for Django project.
    This class is used for setting up and configuring the application in a Django project,
    defining the application name and default behavior.

    :param default_auto_field: The default field type for auto-generated primary keys (BigAutoField)
    :type default_auto_field: str
    :param name: The full name of the application used by Django for its registration
    :type name: str
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'books'

-- Creating a separate database for a Java service
CREATE DATABASE java_books;
GRANT ALL PRIVILEGES ON DATABASE java_books TO book_user;

-- Creating a separate database for the Python service
CREATE DATABASE python_books;
GRANT ALL PRIVILEGES ON DATABASE python_books TO book_user;
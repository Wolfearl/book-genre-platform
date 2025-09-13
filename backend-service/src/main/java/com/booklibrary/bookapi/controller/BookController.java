package com.booklibrary.bookapi.controller;

import com.booklibrary.bookapi.ApiConstants;
import com.booklibrary.bookapi.model.Book;
import com.booklibrary.bookapi.repository.BookRepository;
import io.swagger.v3.oas.annotations.Operation;
import java.util.List;
import java.util.Optional;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * Controller for working with books.
 */
@RestController
@RequestMapping(ApiConstants.API_PREFIX + ApiConstants.BOOKS_ENDPOINT)
public class BookController {
    
    @Autowired
    private BookRepository bookRepository;

    /**
     * Getting all books from the database.
     * Uses {@link com.booklibrary.bookapi.repository.BookRepository} to get all books from the database.
     * 
     * @return {@link org.springframework.http.ResponseEntity} with a list of books and HTTP status
     * @throws Exception in case of data retrieval errors (automatic handling in try-catch)
     */
    @Operation(summary = "Get all books")
    @GetMapping
    public ResponseEntity<List<Book>> getAllBooks() {
        try {
            List<Book> books = bookRepository.findAll();
            if (books.isEmpty()) {
                return new ResponseEntity<>(null, HttpStatus.NO_CONTENT);
            }
            return new ResponseEntity<>(books, HttpStatus.OK);
        } catch (Exception e) {
            return new ResponseEntity<>(null, HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    /**
     * Getting a book from the database by ID.
     * Uses {@link com.booklibrary.bookapi.repository.BookRepository} to find book by ID.
     * 
     * @param id Book ID
     * @return {@link org.springframework.http.ResponseEntity} with a book and HTTP status or only HTTP status
     */
    @Operation(summary = "Get book by ID")
    @GetMapping("/{id}")
    public ResponseEntity<Book> getBookById(@PathVariable("id") long id) {
        Optional<Book> bookData = bookRepository.findById(id);
        return bookData.map(book -> new ResponseEntity<>(book, HttpStatus.OK)).orElseGet(() -> new ResponseEntity<>(HttpStatus.NOT_FOUND));
    }

    /**
     * Creates a new book based on the data passed in the request body.
     * Uses {@link com.booklibrary.bookapi.repository.BookRepository} to save a new book.
     * 
     * @param book An object {@link com.booklibrary.bookapi.model.Book} with data about the book (title, author, year of publication, pages, rating)
     * @return {@link org.springframework.http.ResponseEntity} with the saved book object and HTTP status
     * @throws Exception on save errors (automatic handling in try-catch)
     */
    @Operation(summary = "Create a new book")
    @PostMapping
    public ResponseEntity<Book> createBook(@RequestBody Book book) {
        try {
            Book newBook = bookRepository.save(new Book(book.getTitle(), book.getAuthor(), book.getPublicationYear(), book.getPages(), book.getRating()));
            return new ResponseEntity<>(newBook, HttpStatus.CREATED);
        } catch (Exception e) {
            return new ResponseEntity<>(null, HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    /**
     * Update book data by id with data from the request body.
     * Uses {@link com.booklibrary.bookapi.repository.BookRepository} to find book by ID and save new data.
     * 
     * @param id Book ID
     * @param book And object {@link com.booklibrary.bookapi.model.Book} with new data about the book
     * @return {@link org.springframework.http.ResponseEntity} with updated book data and HTTP status
     */
    @Operation(summary = "Update book by ID")
    @PutMapping("/{id}")
    public ResponseEntity<Book> updateBook(@PathVariable("id") long id, @RequestBody Book book){
        Optional<Book> bookData = bookRepository.findById(id);
        if (bookData.isPresent()) {
            Book existingBook = bookData.get();
            existingBook.setTitle(book.getTitle());
            existingBook.setAuthor(book.getAuthor());
            existingBook.setPublicationYear(book.getPublicationYear());
            return new ResponseEntity<>(bookRepository.save(existingBook) , HttpStatus.OK);
        }
        return new ResponseEntity<>(HttpStatus.NOT_FOUND);
    }

    /**
     * Deleting a book by id
     * Uses {@link com.booklibrary.bookapi.repository.BookRepository} to delete book by ID.
     * 
     * @param id Book ID
     * @return {@link org.springframework.http.ResponseEntity} with HTTP status
     * @throws Exception on delete errors (automatic handling in try-catch)
     */
    @Operation(summary = "Delete book by ID")
    @DeleteMapping("/{id}")
    public ResponseEntity<HttpStatus> deleteBook(@PathVariable("id") long id){
        try {
            bookRepository.deleteById(id);
            return new ResponseEntity<>(HttpStatus.NO_CONTENT);
        } catch (Exception e) {
            return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }    
}

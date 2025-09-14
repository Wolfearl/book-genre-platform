package com.booklibrary.bookapi.config;

import com.booklibrary.bookapi.model.Book;
import com.booklibrary.bookapi.repository.BookRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

/**
 * Initializes the application with sample data.
 */
@Component
public class DataLoader implements CommandLineRunner {

    @Autowired
    private BookRepository bookRepository;

    /**
     * Executes after the application context is loaded.
     * <p>
     * If the book repository is empty, it adds several predefined
     * {@link Book} instances into the database.
     * </p>
     *
     * @param args command-line arguments passed to the application
     * @throws Exception if an error occurs while saving data
     */
    @Override
    public void run(String... args) throws Exception {
        if (bookRepository.count() == 0) {
            bookRepository.save(new Book("Effective Java", "Joshua Bloch", 2018, 416, 5.0));
            bookRepository.save(new Book("Clean Code", "Robert C. Martin", 2008, 464, 5.0));
            bookRepository.save(new Book("Spring in Action", "Craig Walls", 2020, 520, 4.0));
            System.out.println("Added test data to database");
        }
    }
    
}

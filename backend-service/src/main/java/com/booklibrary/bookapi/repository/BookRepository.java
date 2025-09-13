package com.booklibrary.bookapi.repository;

import com.booklibrary.bookapi.model.Book;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

/**
 * Repository for working with the entity {@link Book}.
 * Uses Spring Data JPA for automatic implementation of 
 * basic CRUD operations (create, read, update, delete).
 * The interface extends {@link JpaRepository}, which provides a set of 
 * ready-made methods for data access and management.
 */
@Repository
public interface BookRepository extends JpaRepository<Book, Long>{
     // Spring Data JPA will automatically provide basic CRUD operations.
}

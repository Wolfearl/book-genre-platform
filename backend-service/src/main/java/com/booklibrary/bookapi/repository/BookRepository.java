package com.booklibrary.bookapi.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import com.booklibrary.bookapi.model.Book;

@Repository
public interface BookRepository extends JpaRepository<Book, Long>{
     // Spring Data JPA автоматически предоставит базовые CRUD-операции
}

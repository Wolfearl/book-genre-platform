package com.booklibrary.bookapi.model;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

/**
 * Book entity mapped to the "books" table in the database.
 * Stores basic information about the book: identifier, title, author,
 * year of publication, number of pages and rating.
 */
@Entity
@Table(name = "books")
public class Book {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false)
    private String title;

    @Column(nullable = false)
    private String author;

    @Column(name = "publication_year")
    private Integer publicationYear;

    private Integer pages;

    private Double rating;

    /**
     * Empty constructor required for JPA.
     */
    public Book() {}

    /**
     * Constructor for creating a book with basic parameters.
     * 
     * @param title The title of the book
     * @param author The author of the book
     * @param publicationYear The year of publication
     * @param pages The number of pages
     * @param rating The rating of the book
     */
    public Book(String title, String author, Integer publicationYear, Integer pages, Double rating) {
        this.title = title;
        this.author = author;
        this.publicationYear = publicationYear;
        this.pages = pages;
        this.rating = rating;
    }

    /**
     * Returns the unique identifier of the book.
     * 
     * @return Unique book identifier
     */
    public Long getId() { 
        return id; 
    }
    
    /**
     * Sets a unique identifier for the book.
     * 
     * @param id Unique book identifier
     */
    public void setId(Long id) { 
        this.id = id; 
    }
    
    /**
     * Returns the title of the book.
     * 
     * @return The title of the book
     */
    public String getTitle() { 
        return title; 
    }

    /**
     * Sets the title of the book.
     * 
     * @param title The title of the book
     */
    public void setTitle(String title) { 
        this.title = title; 
    }
    
    /**
     * Returns the author of the book.
     * 
     * @return The author of the book
     */
    public String getAuthor() { 
        return author; 
    }

    /**
     * Sets the author of the book.
     * 
     * @param author The author of the book
     */
    public void setAuthor(String author) { 
        this.author = author; 
    }
    
    /**
     * Returns the year the book was published.
     * 
     * @return The year of publication
     */
    public Integer getPublicationYear() { 
        return publicationYear; 
    }

    /**
     * Sets the publication year of the book.
     * 
     * @param publicationYear The year of publication
     */
    public void setPublicationYear(Integer publicationYear) { 
        this.publicationYear = publicationYear; 
    }

    /**
     * Returns the number of pages in the book.
     * 
     * @return The number of pages
     */
    public Integer getPages() { 
        return pages; 
    }

    /**
     * Sets the number of pages in the book.
     * 
     * @param pages The number of pages
     */
    public void setPages(Integer pages) { 
        this.pages = pages; 
    }

    /**
     * Returns the book rating.
     * 
     * @return The rating of the book
     */
    public Double getRating() { 
        return rating; 
    }

    /**
     * Sets the book rating.
     * 
     * @param rating The rating of the book
     */
    public void setRating(Double rating) { 
        this.rating = rating; 
    }

    /**
     * Returns a string representation of the book with the main fields.
     * 
     * @return a string description of the book
     */
    @Override
    public String toString() {
        return "Book {" +
               "id = " + id +
               ", title = '" + title + '\'' +
               ", author = '" + author + '\'' +
               ", publicationYear = " + publicationYear + '}';
    }
    
}

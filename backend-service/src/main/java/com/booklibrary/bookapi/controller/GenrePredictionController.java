package com.booklibrary.bookapi.controller;

import com.booklibrary.bookapi.ApiConstants;
import com.booklibrary.bookapi.model.Book;
import com.booklibrary.bookapi.service.MLService;
import io.swagger.v3.oas.annotations.Operation;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;


/**
 * Controller for predicting the genre of a book.
 * <p>
 * The controller provides an API endpoint to get the predicted genre.
 * <p>
 * Handles HTTP requests at the path "/api/genres".
 */
@RestController
@RequestMapping(ApiConstants.API_PREFIX + ApiConstants.PREDICT_PREFIX)
public class GenrePredictionController {

    private final MLService mlService;

    /**
     * Constructor of the controller that accepts a machine learning service.
     * 
     * @param mlService Service {@link MLService} for predicting the genre of a book
     */
    public GenrePredictionController(MLService mlService) {
        this.mlService = mlService;
    }

    /**
     * Returns the predicted genre of a book.
     * 
     * @return predicted genre of the book
     */
    @Operation(summary = "Get the predicted book genre")
    @PostMapping(ApiConstants.PREDICT_ENDPOINT)
    public String predictGenre(@RequestBody Book bookData) {
        return mlService.predictGenre(bookData);
    }
}

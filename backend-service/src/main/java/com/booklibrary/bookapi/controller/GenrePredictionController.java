package com.booklibrary.bookapi.controller;

import com.booklibrary.bookapi.ApiConstants;
import com.booklibrary.bookapi.service.MLService;
import io.swagger.v3.oas.annotations.Operation;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

/**
 * Controller for predicting the genre of a book.
 * <p>
 * The controller provides an API endpoint to get the predicted genre
 * based on the book title.
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
     * Returns the predicted genre of a book based on its title.
     * 
     * @param title The book title for predicting the genre
     * @return predicted genre of the book
     */
    @Operation(summary = "Get the predicted book genre")
    @GetMapping(ApiConstants.PREDICT_ENDPOINT)
    public String predictGenre(@RequestParam String title) {
        return mlService.predictGenre(title);
    }
}

package com.booklibrary.bookapi.service;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

/**
 * Service for interaction with an external machine learning API.
 * <p>
 * Uses {@link RestTemplate} to send HTTP requests
 * and receive book genre predictions based on the title.
 * <p>
 * The service URL is specified via the configuration parameter "ml.service.url".
 */
@Service
public class MLService {

    @Value("${ml.service.url:http://localhost:8000/}")
    private String mlServiceUrl;

    private RestTemplate restTemplate;

    /**
     * Constructor that initializes the {@link RestTemplate}.
     * 
     * @param restTemplate Client for executing HTTP requests
     */
    public MLService(RestTemplate restTemplate) {
        this.restTemplate = restTemplate;
    }

    /**
     * Sends a request to an ML service to predict the genre based on the book title.
     * 
     * @param bookTitle The book title for predicting the genre
     * @return Predicted genre as a string or a connection error message
     */
    public String predictGenre(String bookTitle) {
        try {
            String url = mlServiceUrl + "api/predict?title=" + bookTitle;
            return restTemplate.getForObject(url, String.class);
        } catch (Exception e) {
            return "Error connecting to ML service: " + e.getMessage();
        }
    }
    
}

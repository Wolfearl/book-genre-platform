package com.booklibrary.bookapi.service;

import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;
import org.springframework.web.client.RestTemplate;
import com.booklibrary.bookapi.model.Book;
import com.fasterxml.jackson.databind.ObjectMapper;


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
    public MLService(RestTemplate restTemplate, ObjectMapper objectMapper) {
        this.restTemplate = restTemplate;
    }

    /**
     * Sends a request to an ML service to predict the genre.
     * 
     * @return Predicted genre as a string or a connection error message
     */
    public String predictGenre(Book bookData) {
        try {
            String url = mlServiceUrl + "api/predict/";

            HttpHeaders headers = new HttpHeaders();
            headers.setContentType(MediaType.APPLICATION_FORM_URLENCODED);

            MultiValueMap<String, Object> body = new LinkedMultiValueMap<>();
            
            if (bookData.getTitle() != null) {
                body.add("title", bookData.getTitle());
            }
            if (bookData.getDescription() != null) {
                body.add("description", bookData.getDescription());
            }
            if (bookData.getRating() != null) {
                body.add("rating", bookData.getRating().toString());
            }

            HttpEntity<MultiValueMap<String, Object>> request = new HttpEntity<>(body, headers);
            ResponseEntity<String> response = restTemplate.postForEntity(url, request, String.class);
            
            if (response.getStatusCode().is2xxSuccessful()) {
                return response.getBody();
            } else {
                return "Error from ML service: " + response.getStatusCode() + " - " + response.getBody();
            }
        } catch (Exception e) {
            return "Error connecting to ML service: " + e.getMessage();
        }
    }
    
}

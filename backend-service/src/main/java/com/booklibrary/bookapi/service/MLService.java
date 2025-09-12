package com.booklibrary.bookapi.service;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
public class MLService {

    @Value("${ml.service.url:http://localhost:8000/}")
    private String mlServiceUrl;

    private RestTemplate restTemplate;

    public MLService(RestTemplate restTemplate) {
        this.restTemplate = restTemplate;
    }

    public String predictGenre(String bookTitle) {
        try {
            String url = mlServiceUrl + "api/predict?title=" + bookTitle;
            return restTemplate.getForObject(url, String.class);
        } catch (Exception e) {
            return "Error connecting to ML service: " + e.getMessage();
        }
    }
    
}

package com.booklibrary.bookapi.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.client.RestTemplate;

/**
 * Spring configuration class defining beans for the application context.
 */
@Configuration
public class RestTemplateConfig {
    
    /**
     * Creates and returns a bean of type {@link RestTemplate}.
     * 
     * @return A new instance of {@link RestTemplate} for making HTTP requests
     */
    @Bean
    public RestTemplate restTemplate() {
        return new RestTemplate();
    }
}

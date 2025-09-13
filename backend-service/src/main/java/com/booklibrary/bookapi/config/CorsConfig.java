package com.booklibrary.bookapi.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

import com.booklibrary.bookapi.ApiConstants;

/**
 * Spring configuration class responsible for setting up CORS (Cross-Origin Resource Sharing).
 */
@Configuration
public class CorsConfig {

    /**
     * Creates a bean of type {@link WebMvcConfigurer} that configures CORS rules for all URLs with the prefix {@code /api/}.
     * <p>
     * The configuration allows requests from the domain {@code http://localhost:8000} with methods {@code GET}, {@code POST}, {@code PUT},
     * {@code DELETE}, and {@code OPTIONS}, permits all headers, and also allows sending cookies and authorization data.
     *
     * @return A configured {@link WebMvcConfigurer} with CORS rules
     */
    @Bean
    public WebMvcConfigurer corsConfigurer() {
        return new WebMvcConfigurer() {
            @Override
            public void addCorsMappings(CorsRegistry registry) {
                registry.addMapping("**"+ ApiConstants.API_PREFIX +"/**")            // for all URLs with /api/*
                        .allowedOrigins("http://localhost:8000")                     // allowed domain
                        .allowedMethods("GET", "POST", "PUT", "DELETE", "OPTIONS")   // allowed HTTP methods
                        .allowedHeaders("*")                                         // all headers allowed
                        .allowCredentials(true);                                     // allow cookies, authorization data
            }
        };
    } 
    
}

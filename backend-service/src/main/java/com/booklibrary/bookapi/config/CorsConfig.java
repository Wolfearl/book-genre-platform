package com.booklibrary.bookapi.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
public class CorsConfig {

    @Bean
    public WebMvcConfigurer corsConfigurer() {
        return new WebMvcConfigurer() {
            @Override
            public void addCorsMappings(CorsRegistry registry) {
                registry.addMapping("**/api/**")                                     // для всех URL с /api/*
                        .allowedOrigins("http://localhost:8000")                     // разрешён домен
                        .allowedMethods("GET", "POST", "PUT", "DELETE", "OPTIONS")   // разрешённые HTTP-методы
                        .allowedHeaders("*")                                         // разрешены все заголовки
                        .allowCredentials(true);                                     // разрешить куки, авторизационные данные
            }
        };
    } 
    
}

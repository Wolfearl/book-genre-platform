package com.booklibrary.bookapi.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.booklibrary.bookapi.service.MLService;

import io.swagger.v3.oas.annotations.Operation;

@RestController
@RequestMapping("/api/genres")
public class GenrePredictionController {

    private final MLService mlService;

    public GenrePredictionController(MLService mlService) {
        this.mlService = mlService;
    }

    // GET предсказанный жанр книги
    @Operation(summary = "Get the predicted book genre")
    @GetMapping("/predictGenre")
    public String predictGenre(@RequestParam String title) {
        return mlService.predictGenre(title);
    }
}

package com.booklibrary.bookapi.controller;

import com.booklibrary.bookapi.ApiConstants;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;


/**
 * REST controller for checking the server readiness state.
 * <p>
 * Uses JdbcTemplate to execute a test query against the database.
 */
@RestController
@RequestMapping(ApiConstants.API_PREFIX + ApiConstants.HEALTH_ENDPOINT)
public class HealthController {
    
    @Autowired
    private JdbcTemplate jdbcTemplate;

    /**
     * Checks the status of the database connection.
     * Executes a simple {@code SELECT 1} query to ensure that the connection is active.
     * 
     * @return A string with the result of the check
     */
    @GetMapping("/db")
    public String checkDbConnection() {
        try {
            jdbcTemplate.execute("SELECT 1");
            return "Database connection is OK";
        } catch (Exception e) {
            return "Database connection failed: " + e.getMessage();
        }
    }
    
}

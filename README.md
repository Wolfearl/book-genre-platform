# Book Genre ML Platform

[![Java](https://img.shields.io/badge/Java-24.0.1-blue.svg)](https://www.java.com/)
[![Spring Boot](https://img.shields.io/badge/Spring%20Boot-3.5.5-brightgreen.svg)](https://spring.io/projects/spring-boot)
[![Python](https://img.shields.io/badge/Python-3.12.5-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.2.6-green.svg)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/DRF-3.16.1-red.svg)](https://www.django-rest-framework.org/)
[![Postman](https://img.shields.io/badge/Postman-11.62.4-orange.svg)](https://www.postman.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A training project that serves as a platform for managing books and predicting their genres using machine learning. It is built with a microservices architecture, leveraging Java Spring Boot and Python Django.

## 📋 Table of Contents

- [Architecture](#-architecture)
- [Technology stack](#-technology-stack)
- [Functionality](#-functionality)
- [Installation and launch](#-installation-and-launch)
- [API](#-api)
- [License](#-license)
- [Progress](#-progress)
- [Testing the Integration](#-testing-the-integration)
- [Troubleshooting](#-troubleshooting)

## 🏗️ Architecture

The project employs a microservices architecture to ensure scalability and flexibility:

```plaintext
book-genre-platform/
├── backend-service/          # Java microservice (Spring Boot) – The main API for CRUD operations with books
├── ml-service/               # Python microservice (Django) – Microservice for ML predictions
├── infrastructure/           # Docker Compose configuration for orchestrating services
├── algorithms/               # Solving algorithmic problems using Python and Java
├── docs/                     # Additional Documentation
├── integration-test.sh       # Script for integration testing
└── README.md                 # This file
```

```mermaid
graph TD
    Client[Web Client] --> JavaAPI[Java Spring Boot API]
    Client --> PythonAPI[Python Django API]
    JavaAPI --> JavaDB[(H2 Database)]
    PythonAPI --> PythonDB[(SQLite Database)]
    JavaAPI -.-> PythonAPI
```

## 🛠️ Technology stack

### Backend Service (Java)

- Java 24.0.1
- Spring Boot 3.5.5
- Spring Data JPA - for working with the database
- H2 Database - embedded database for development
- Maven - for project build purposes

### ML Service (Python)

- Python 3.12.5
- Django 5.2.6 - web framework
- Django REST Framework (DRF) - for building a REST API
- SQLite - the default database for development
- Pip - for dependency management

### General Tools

- Git - version control
- Docker - containerization
- Docker Compose - container orchestration
- Postman - API testing

### 📊 Functionality

### Current Functionality (Week 1)

- Backend Service: CRUD operations for books (create, read, update, delete) via REST API
- ML Service:  CRUD operations for books (create, read, update, delete) via REST API, search for similar books
- Interaction between microservices

### Planned Functionality

- Integration of an ML model for book genre prediction
- Application containerization using Docker
- CI/CD setup with GitHub Actions

## 🚀 Installation and launch

### Prerequisites

- Install Java 24.0.1 or OpenJDK 24
- Install Python 3.12.5
- Install Git

### Starting the Backend Service (Java)

```bash
cd backend-service
./mvnw spring-boot:run
```

The service will be accessible at the following address: http://localhost:8080

### Starting the ML Service (Python)

1. Go to the directory ml-service:
```bash
cd ml-service
```
2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate   # for Linux/macOS
# or
venv\Scripts\activate      # for Windows
```
3. Install the dependencies:
```bash
pip install -r requirements.txt
```
4. Apply the migrations:
```bash
python manage.py migrate
```
5. Start the server:
```bash
python manage.py runserver
```

The service will be accessible at the following address: http://localhost:8000

## 📡 API

### Backend Service (Java)

- GET /api/books - Get all books
- POST /api/books - Create a new book
- GET /api/books/{id} - Get book by ID
- PUT /api/books/{id} - Update book by ID
- DELETE /api/books/{id} - Delete a book by ID
- GET /api/genres/predictGenre - Get the predicted book genre

Example of a request body for creating a book (JSON):
```json
{
  "title": "The title of the book",
  "author": "The author of the book",
  "publicationYear": 2023,
  "pages": 120,
  "rating": 4.1
}
```

Example of an HTTP request for genre prediction:
```bash
curl http://localhost:8080/api/genres/predictGenre?title=Python+Programming
```

### ML Service (Python)

- GET /api/books/ - Get all books
- POST /api/books/ - Create a new book
- GET /api/books/{id}/ - Get book by ID
- PUT /api/books/{id}/ - Update book by ID
- DELETE /api/books/{id}/ - Delete a book by ID
- GET /api/predict?title=Book+Title - Predict genre
- GET /api/books/similar/{book_id}/ - Get similar books

Example of a request body for creating a book (JSON):
```json
{
  "title": "The title of the book",
  "author": "The author of the book",
  "publication_year": 2022,
  "pages": 240,
  "rating": 4.2
}
```

Example of an HTTP request for genre prediction:
```bash
curl http://localhost:8000/api/predict?title=Python+Programming
```

## 📄 License
This project is licensed under the MIT License. For more details, please refer to the LICENSE file.

## 📊 Progress

### Week 1 Completion Status

#### Python/Django Service
- [x] Project setup and configuration
- [x] Data models and migrations
- [x] REST API endpoints
- [x] Serializers and views
- [ ] Tests (0% covered)

#### Java/Spring Boot Service
- [x] Project setup with Spring Initializr
- [x] JPA entities and repositories
- [x] REST controllers
- [x] Basic error handling
- [ ] Tests (0% covered)

#### General Skills
- [x] Linear algebra fundamentals for ML
- [x] Reading technical documentation in English
- [x] Solving algorithmic problems on LeetCode
- [x] API documentation with Swagger/OpenAPI
- [x] Project documentation best practices

#### Week 1 Statistics
- Commits: 10+
- Hours spent: 35-40
- LeetCode problems solved: 5

## 🧪 Testing the Integration

1. Start both services
2. Predict genre using the Python service from Java service:
```bash
curl http://localhost:8080/api/genres/predictGenre?title=Python+Programming
```

## 🐛 Troubleshooting

### Port Already in Use Error

If port 8080 or 8000 is occupied, change the port in the settings:

**Java-service**: add to application.properties:
```properties
server.port=8081
```
**Python-service**: run with a different port:
```bash
python manage.py runserver 8001
```

### Database connection errors

Make sure that the database is running and accessible.
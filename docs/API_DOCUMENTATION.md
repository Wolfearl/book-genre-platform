# API Documentation

## Java Backend Service (Port 8080)

### GET /api/books
Returns all books in the database.

**Response:**
```json
[
  {
    "id": 1,
    "title": "Example Book 1",
    "author": "John Doe",
    "publicationYear": 2023
  }
]
```

### GET /api/books/{id}
Get book by ID.

**Response:**
```json
[
  {
    "id": 2,
    "title": "Example Book 2",
    "author": "Jane Smith",
    "publicationYear": 2020
  }
]
```

### POST /api/books
Creates a new book.

**Request Body:**
```json
[
  {
    "id": 3,
    "title": "New Book",
    "author": "Johnzon Williams",
    "publicationYear": 2023
  }
]
```

### PUT /api/books/{id}
Update book by ID.

**Request Body:**
```json
[
  {
    "id": 3,
    "title": "New Book",
    "author": "Johnson Williams",
    "publicationYear": 2023
  }
]
```

### DELETE /api/books/{id}
Delete book by ID.

### GET /api/genres/predictGenre
Get the predicted book genre.

Parameters:
- **title** (string): The book title
- **description** (string): The book description
- **rating** (float): The book rating

**Response:**
```json
[
  {
    "title": "Shadows Over Skyline",
    "description": "In the bustling metropolis of Skyline City, a determined detective and a tech-savvy journalist team up to uncover a sprawling conspiracy that threatens the very fabric of their society. Against a backdrop of political corruption, high-stakes corporate warfare, and deep personal secrets, they must use their skills, wit, and courage to expose the truth. Combining elements of thriller, crime, and political drama, this gripping tale explores themes of justice, trust, and resilience in a modern urban setting.",
    "rating": 4.0,
    "predicted_genre": "Fiction"
  }
]
```

</br>

## Python ML Service (Port 8000)

### GET /api/books/similar/{book_id}/
Get similar books.

**Response:**
```json
[
  {
    "id": 1,
    "title": "Example Book 1",
    "author": "John Doe",
    "publicationYear": 2023
  },
  {
    "id": 4,
    "title": "Example Book 4",
    "author": "Johnson Doe",
    "publicationYear": 2022
  },
  {
    "id": 10,
    "title": "Example Book 10",
    "author": "Jay Don",
    "publicationYear": 2024
  }
]
```

### GET /api/predict
Predicts genre based on book title.

Parameters:
 - **title** (string): The book title

**Response:**
```json
[
  {
    "title": "Shadows Over Skyline",
    "description": "In the bustling metropolis of Skyline City, a determined detective and a tech-savvy journalist team up to uncover a sprawling conspiracy that threatens the very fabric of their society. Against a backdrop of political corruption, high-stakes corporate warfare, and deep personal secrets, they must use their skills, wit, and courage to expose the truth. Combining elements of thriller, crime, and political drama, this gripping tale explores themes of justice, trust, and resilience in a modern urban setting.",
    "rating": 4.0,
    "predicted_genre": "Fiction"
  }
]
```
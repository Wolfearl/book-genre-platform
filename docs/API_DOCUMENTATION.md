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

### POST /api/genres/predictGenre
Get the predicted book genre.

Parameters:
- **title** (string): The book title
- **description** (string): The book description
- **rating** (float): The book rating

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

### POST /api/predict
Predicts genre based on book title.

</br>

# ML API Documentation

## Endpoints

### POST /api/predict/
Genre prediction for one book.

**Request Body:**
```json
{
  "title": "Shadows Over Skyline",
  "description": "In the bustling metropolis of Skyline City, a determined detective and a tech-savvy journalist team up to uncover a sprawling conspiracy that threatens the very fabric of their society. Against a backdrop of political corruption, high-stakes corporate warfare, and deep personal secrets, they must use their skills, wit, and courage to expose the truth. Combining elements of thriller, crime, and political drama, this gripping tale explores themes of justice, trust, and resilience in a modern urban setting.",
  "rating": 4.0
}
```
**Response:**

```json
{
    "genre": "('Fiction', 'Mystery', 'Mystery Thriller', 'Thriller')",
    "probabilities": [
        [
            "Fiction",
            "0.8732579013222905"
        ],
        [
            "Mystery",
            "0.7823685054140499"
        ],
        [
            "Thriller",
            "0.7329521564703759"
        ]
    ],
    "prediction_time": 1.5169,
    "cached": true,
    "features_used": {
        "title_length": 20,
        "description_length": 509,
        "has_description": true
    }
}
```

### POST /api/predict/batch/

Batch prediction for multiple books.

**Request Body:**
```json
{
  "books": [
    {
      "title": "Shadows Over Skyline",
      "description": "In the bustling metropolis of Skyline City, a determined detective and a tech-savvy journalist team up to uncover a sprawling conspiracy that threatens the very fabric of their society. Against a backdrop of political corruption, high-stakes corporate warfare, and deep personal secrets, they must use their skills, wit, and courage to expose the truth. Combining elements of thriller, crime, and political drama, this gripping tale explores themes of justice, trust, and resilience in a modern urban setting.",
      "rating": 4
    },
    {
      "title": "Whispers of the Forest",
      "description": "A young botanist ventures into an ancient forest with a mysterious past, uncovering secrets about nature, magic, and her own heritage. Faced with challenges and mystical creatures, she must find a way to restore balance to the forest and protect its wonders. This story blends fantasy, adventure, and personal growth.",
      "rating": 3.5
    },
    {
      "title": "Echoes of Tomorrow",
      "description": "Set in a dystopian future, a scientist struggles against time to prevent a global catastrophe. Themes of technology, ethics, and hope intertwine in this gripping science fiction narrative.",
      "rating": 4.7
    }
  ]
}
```
**Response:**

```json
{
    "results": [
        {
            "genre": [
                "Fiction",
                "Mystery",
                "Mystery Thriller",
                "Thriller"
            ],
            "probabilities": [
                [
                    "Fiction",
                    0.8732579013222905
                ],
                [
                    "Mystery",
                    0.7823685054140499
                ],
                [
                    "Thriller",
                    0.7329521564703759
                ]
            ],
            "prediction_time": 1.5169,
            "cached": true,
            "features_used": {
                "title_length": 20,
                "description_length": 509,
                "has_description": true
            }
        },
        {
            "genre": [
                "Fantasy",
                "Fiction"
            ],
            "probabilities": [
                [
                    "Fantasy",
                    0.887423066086662
                ],
                [
                    "Fiction",
                    0.8113413424490749
                ],
                [
                    "Young Adult",
                    0.3832622790504535
                ]
            ],
            "prediction_time": 0.2914,
            "cached": true,
            "features_used": {
                "title_length": 22,
                "description_length": 317,
                "has_description": true
            }
        },
        {
            "genre": [
                "Fiction",
                "Science Fiction"
            ],
            "probabilities": [
                [
                    "Science Fiction",
                    0.8416041591837881
                ],
                [
                    "Fiction",
                    0.6553569185868126
                ],
                [
                    "Fantasy",
                    0.3843910685036882
                ]
            ],
            "prediction_time": 0.2864,
            "cached": true,
            "features_used": {
                "title_length": 18,
                "description_length": 188,
                "has_description": true
            }
        }
    ],
    "batch_stats": {
        "total": 3,
        "successful": 3,
        "failed": 0,
        "processing_time": 0.0009982585906982422
    }
}
```

### GET /api/model/info/

Information about the uploaded ML model.

### GET /api/predictions/stats/

Prediction statistics.

### GET /api/health/

Checking the health of the service.
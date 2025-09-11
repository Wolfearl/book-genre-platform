# Book Genre ML Platform

[![Java](https://img.shields.io/badge/Java-24.0.1-blue.svg)](https://www.java.com/)
[![Spring Boot](https://img.shields.io/badge/Spring%20Boot-3.5.5-brightgreen.svg)](https://spring.io/projects/spring-boot)
[![Python](https://img.shields.io/badge/Python-3.12.5-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.2.6-green.svg)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/DRF-3.16.1-red.svg)](https://www.django-rest-framework.org/)
[![Postman](https://img.shields.io/badge/Postman-11.62.4-orange.svg)](https://www.postman.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Учебный проект, представляющий собой платформу для управления книгами и предсказания их жанров с помощью машинного обучения. Построен по микросервисной архитектуре с использованием Java Spring Boot и Python Django.

## 📋 Оглавление

- [Архитектура](#-архитектура)
- [Технологический стек](#-технологический-стек)
- [Функциональность](#-функциональность)
- [Установка и запуск](#-установка-и-запуск)
- [API](#-api)
- [Лицензия](#-лицензия)
- [Прогресс](#-прогресс)

## 🏗️ Архитектура

Проект использует микросервисную архитектуру для обеспечения масштабируемости и гибкости:

```plaintext
book-genre-platform/
├── backend-service/          # Java-микросервис (Spring Boot) - Основной API для CRUD операций с книгами
├── ml-service/               # Python-микросервис (Django) - Микросервис для ML-предсказаний
├── infrastructure/           # Конфигурация Docker Compose для оркестрации сервисов
├── algorithms/               # Решение алгоритмических задач на Python и Java
├── docs/                     # Дополнительная документация
└── README.md                 # Этот файл
```

## 🛠️ Технологический стек

### Backend Service (Java)

- Java 24.0.1
- Spring Boot 3.5.5
- Spring Data JPA - для работы с базой данных
- H2 Database - встроенная БД для разработки
- Maven - для сборки проекта

### ML Service (Python)

- Python 3.12.5
- Django 5.2.6 - веб-фреймворк
- Django REST Framework (DRF) - для создания REST API
- SQLite - база данных по умолчанию для разработки
- Pip - для управления зависимостями

### Общие инструменты

- Git - контроль версий
- Docker - контейнеризация
- Docker Compose - оркестрация контейнеров
- Postman - тестирование API

### 📊 Функциональность

### Текущая функциональность (Неделя 1)

- Backend Service: CRUD операции для книг (создание, чтение, обновление, удаление) через REST API
- ML Service: CRUD операции для книг (создание, чтение, обновление, удаление) через REST API

### Планируемая функциональность

- Интеграция ML-модели для предсказания жанра книги
- Взаимодействие между микросервисами
- Контейнеризация приложений с помощью Docker
- Настройка CI/CD с помощью GitHub Actions

## 🚀 Установка и запуск

### Предварительные требования

- Установите Java 24.0.1 или OpenJDK 24
- Установите Python 3.12.5
- Установите Git

### Запуск Backend Service (Java)

1. Перейдите в директорию backend-service:
```bash
cd backend-service
```
2. Соберите проект с помощью Maven:
```bash
./mvnw clean package
```
3. Запустите приложение.

Сервис будет доступен по адресу: http://localhost:8080

### Запуск ML Service (Python)

1. Перейдите в директорию ml-service:
```bash
cd ml-service
```
2. Создайте виртуальное окружение и активируйте его:
```bash
python -m venv venv
source venv/bin/activate   # для Linux/macOS
# или
venv\Scripts\activate      # для Windows
```
3. Установите зависимости:
```bash
pip install -r requirements.txt
```
4. Примените миграции:
```bash
python manage.py migrate
```
5. Запустите сервер:
```bash
python manage.py runserver
```

Сервис будет доступен по адресу: http://localhost:8000

## 📡 API

### Backend Service (Java)

- GET /api/books - получить список всех книг
- POST /api/books - создать новую книгу
- GET /api/books/{id} - получить книгу по ID
- PUT /api/books/{id} - обновить книгу по ID
- DELETE /api/books/{id} - удалить книгу по ID

Пример тела запроса для создания книги (JSON):
```json
{
  "title": "Название книги",
  "author": "Автор книги",
  "publicationYear": 2023
}
```

### ML Service (Python)

- GET /api/books/ - получить список всех книг
- POST /api/books/ - создать новую книгу
- GET /api/books/{id}/ - получить книгу по ID
- PUT /api/books/{id}/ - обновить книгу по ID
- DELETE /api/books/{id}/ - удалить книгу по ID

Пример тела запроса для создания книги (JSON):
```json
{
  "title": "Название книги",
  "author": "Автор книги",
  "publication_year": 2023
}
```

## 📄 Лицензия
Этот проект распространяется под лицензией MIT. Подробнее см. в файле LICENSE.

## 📊 Прогресс

### День 5: English & Algorithms

#### English Practice
- Studied Django documentation: [Writing your first Django app](https://docs.djangoproject.com/en/stable/intro/tutorial01/)
- Studied Spring Boot documentation: [Building a RESTful Web Service](https://spring.io/guides/gs/rest-service/)

#### Algorithms Solved ([LeetCode](https://leetcode.com/))
- [Two Sum](https://leetcode.com/problems/two-sum/) - Easy
- [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) - Easy
- [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) - Easy
- [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) - Easy
- [Reverse String](https://leetcode.com/problems/reverse-string/) - Easy

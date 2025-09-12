# Detailed Setup Instructions

## Java Backend Service Setup

1. Install Java 24 SDK
2. Install Maven
3. Navigate to backend-service directory
4. Build: `mvn clean package`
5. Run: `java -jar target/bookapi-0.0.1-SNAPSHOT.jar`

## Python ML Service Setup

1. Install Python 3.12.5
2. Navigate to ml-service directory
3. Create virtual environment: `python -m venv venv`
4. Activate virtual environment:
   - Linux/Mac: `source venv/bin/activate`
   - Windows: `venv\Scripts\activate`
5. Install dependencies: `pip install -r requirements.txt`
6. Run migrations: `python manage.py migrate`
7. Start server: `python manage.py runserver`
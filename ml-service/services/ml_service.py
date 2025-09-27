import logging
import time
from typing import Dict, List
import pandas as pd
import joblib
from django.core.cache import cache

logger = logging.getLogger(__name__)


class MLService:
    def __init__(self):
        self.model = None
        self.multi_label_encoder = None
        self.is_loaded = False
        self.load_model()

    def load_model(self):
        """Loading the model and multi-label encoder"""
        try:
            start_time = time.time()
            self.model = joblib.load('data/models/book_genre_classifier.pkl')
            self.multi_label_encoder = joblib.load('data/models/label_encoder.pkl')
            self.is_loaded = True
            load_time = time.time() - start_time
            logger.info(f"ML model loaded successfully in {load_time:.2f} seconds")
        except Exception as e:
            logger.error(f"Error loading the ML model: {e}")
            self.is_loaded = False

    def preprocess_input(self, title: str, description: str = "",
                         rating: float = 0) -> Dict:
        """Preprocessing the input data for the model"""
        # Data cleaning and validation
        title = title.strip() if title else ""
        description = description.strip() if description else ""

        # Calculation of additional features
        title_length = len(title)
        description_length = len(description)

        # Validation of numeric field
        rating = max(0, min(5, rating))  # Rating limit from 0 to 5

        return {
            'Book': title,
            'Description': description,
            'Avg_Rating': rating,
            'Title_Length': title_length,
            'Description_Length': description_length,
        }

    def predict_single(self, title: str, description: str = "",
                       rating: float = 0) -> Dict:
        """A prediction for one book"""
        if not self.is_loaded:
            return {'error': 'ML model is not loaded'}

        try:
            # Checking the cache
            cache_key = f"prediction_{hash(title + description)}"
            cached_result = cache.get(cache_key)
            if cached_result:
                logger.info("Cached prediction is used")
                return {**cached_result, 'cached': True}

            # Data preprocessing
            processed_data = self.preprocess_input(title, description, rating)

            # Creating a DataFrame for a model
            data_df = pd.DataFrame([processed_data])

            # Prediction
            start_time = time.time()
            prediction = self.model.predict(data_df)
            probabilities = self.model.predict_proba(data_df)
            prediction_time = time.time() - start_time

            # Post-processing of results
            genre = self.multi_label_encoder.inverse_transform(prediction)[0]
            probabilities_dict = {
                self.multi_label_encoder.classes_[i]: float(prob)
                for i, prob in enumerate(probabilities[0])
            }

            # Sorting by probability
            sorted_probs = sorted(
                probabilities_dict.items(), key=lambda x: x[1], reverse=True
            )

            result = {
                'genre': genre,
                'probabilities': sorted_probs[:3],  # Top 3 genres
                'prediction_time': round(prediction_time, 4),
                'cached': False,
                'features_used': {
                    'title_length': processed_data['Title_Length'],
                    'description_length': processed_data['Description_Length'],
                    'has_description': bool(description)
                }
            }

            # Caching the result for 1 hour
            cache.set(cache_key, result, 3600)

            logger.info(f"The prediction was completed in {prediction_time:.4f}s: {genre}")
            return result

        except Exception as e:
            logger.error(f"Prediction error: {e}")
            return {'error': f'Prediction error: {str(e)}'}

    def predict_batch(self, books_data: List[Dict]) -> List[Dict]:
        """Batch prediction for multiple books"""
        if not self.is_loaded:
            return [{'error': 'ML model is not loaded'} for _ in books_data]

        results = []
        for book_data in books_data:
            result = self.predict_single(
                title=book_data.get('title', ''),
                description=book_data.get('description', ''),
                rating=book_data.get('rating', 0),
            )
            results.append(result)

        return results

    def get_model_info(self) -> Dict:
        """Information about the uploaded model"""
        if not self.is_loaded:
            return {'status': 'not_loaded'}

        return {
            'status': 'loaded',
            'model_type': type(self.model.named_steps['classifier']).__name__,
            'classes_count': len(self.multi_label_encoder.classes_),
            'classes': self.multi_label_encoder.classes_.tolist()
        }


# Global instance of the service
ml_service = MLService()
from django.test import TestCase
from services.ml_service import MLService
from books.serializers import PredictionRequestSerializer


class MLServiceTestCase(TestCase):
    def setUp(self):
        self.ml_service = MLService()

    def test_model_loading(self):
        """Model loading test"""
        self.assertTrue(self.ml_service.is_loaded)

    def test_preprocess_input(self):
        """Input data preprocessing test"""
        result = self.ml_service.preprocess_input(
            title="  Test Book  ",
            description="  A test description  ",
            rating=4.5,
        )

        self.assertEqual(result['Book'], "Test Book")
        self.assertEqual(result['Description'], "A test description")
        self.assertEqual(result['Avg_Rating'], 4.5)
        self.assertEqual(result['Title_Length'], 9)
        self.assertEqual(result['Description_Length'], 18)

    def test_predict_single(self):
        """Prediction test for one book"""
        result = self.ml_service.predict_single(
            title="Python Programming Guide"
        )

        self.assertIn('genre', result)
        self.assertIn('probabilities', result)
        self.assertIn('prediction_time', result)


class SerializerTestCase(TestCase):
    def test_prediction_request_serializer(self):
        """Prediction Query Serializer test"""
        # Valid data
        valid_data = {
            'title': 'Test Book',
            'description': 'A test book',
            'rating': 4.5,
        }
        serializer = PredictionRequestSerializer(data=valid_data)
        self.assertTrue(serializer.is_valid())

        # Invalid data
        invalid_data = {
            'title': '',  # Empty name
            'rating': 6.0  # Out-of-range rating
        }
        serializer = PredictionRequestSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
import joblib
import pandas as pd


class BookGenrePredictor:
    """
    A class to predict book genres based on title, description, and additional features using a trained model.

    :param model: loaded trained model for genre classification
    :type model: sklearn.base.BaseEstimator
    :param multi_label_binarizer: encoder to transform genre labels
    :type multi_label_binarizer: sklearn.preprocessing.MultiLabelBinarizer
    """
    def __init__(self, model_path='data/models/book_genre_classifier.pkl'):
        """
        Initializes the BookGenrePredictor by loading the model and multi-label binarizer.

        :param model_path: path to the model pickle file
        :type model_path: str
        """
        self.model = joblib.load(model_path)
        self.multi_label_binarizer = joblib.load('data/models/label_encoder.pkl')

    def predict(self, title, description="", title_length=0, description_length=0, rating=0.0):
        """
        Predicts top genres for a book given its title, description, and features

        :param title: the title of the book
        :type title: str
        :param description: the description or summary of the book. Defaults to empty string
        :type description: str, optional
        :param title_length: length of the book title (number of characters). Defaults to 0
        :type title_length: int, optional
        :param description_length: length of the description (number of characters). Defaults to 0
        :type description_length: int, optional
        :param rating: average rating of the book. Defaults to 0.0
        :type rating: float, optional
        :return: dictionary containing predicted genres and their probabilities (top 3)
        :rtype: dict with keys 'genre' (tuple) and 'probabilities' (list of tuples)
        """
        # Creating a DataFrame with prediction data
        data = pd.DataFrame({
            'Book': [title],
            'Description': [description],
            'Title_Length': [title_length],
            'Description_Length': [description_length],
            'Avg_Rating': [rating],
        })

        # Prediction
        prediction = self.model.predict(data)
        probability = self.model.predict_proba(data)

        # Getting genre and probabilities
        genre = self.multi_label_binarizer.inverse_transform(prediction)[0]
        probabilities = {
            self.multi_label_binarizer.classes_[i]: prob
            for i, prob in enumerate(probability[0])
        }

        # Sorting probabilities in descending order
        sorted_probabilities = sorted(
            probabilities.items(), key=lambda x: x[1], reverse=True
        )

        return {
            'genre': genre,
            'probabilities': sorted_probabilities[:3]  # Top 3 genres
        }


# Example of giants
if __name__ == "__main__":
    predictor = BookGenrePredictor()

    # Testmate example
    result = predictor.predict(
        title="Shadows Over Skyline",
        description=
        """
        In the bustling metropolis of Skyline City, a determined detective and a tech-savvy journalist team up to 
        uncover a sprawling conspiracy that threatens the very fabric of their society. Against a backdrop of 
        political corruption, high-stakes corporate warfare, and deep personal secrets, they must use their skills, 
        wit, and courage to expose the truth. This gripping tale explores themes of justice, trust, and resilience in 
        a modern urban setting.
        """,
        title_length=22,
        description_length=498,
        rating=4.5
    )

    print("Prediction genre:")
    print(f"Main genre: {result['genre']}")
    print("Probabilities by genre:")
    for genre, prob in result['probabilities']:
        print(f"  {genre}: {prob:.4f}")
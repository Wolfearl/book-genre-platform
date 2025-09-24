import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
nltk.data.path.append('D:/Python/nltk_data')

# Loading stopwords and NLTK resources (run once)
nltk.download('punkt', download_dir='D:/Python/nltk_data')
nltk.download('stopwords', download_dir='D:/Python/nltk_data')
nltk.download('wordnet', download_dir='D:/Python/nltk_data')
nltk.download('punkt_tab', download_dir='D:/Python/nltk_data')

class TextPreprocessor:
    """
    A class for preprocessing text data.
    """
    def __init__(self):
        """
        Initializes sets of stop words and a lemmatizer object.
        """
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer =  WordNetLemmatizer()

    def clean_text(self, text):
        """
        Preprocesses the input text.

        :param text: Text to process
        :type text: str
        :return: Preprocessed text, cleaned and lemmatized
        :rtype: str
        """
        text = text.lower()
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        tokens = word_tokenize(text)
        # Stop word removal and lemmatization
        tokens = [self.lemmatizer.lemmatize(token) for token in tokens if token not in self.stop_words]
        return ' '.join(tokens)

    def preprocess_dataframe(self, df, text_columns):
        """
        Applies the clean_text function to all specified text columns of the DataFrame.

        :param df: Source DataFrame with text data
        :type df: pandas.DataFrame
        :param text_columns: List of column names with text for preprocessing
        :type text_columns: list of str
        :return: A copy of the DataFrame with preprocessed text columns
        :rtype: pandas.DataFrame
        """
        processed_df = df.copy()
        for col in text_columns:
            if col in processed_df.columns:
                processed_df[col] = processed_df[col].apply(self.clean_text)
        return processed_df

# Usage example
if __name__ == "__main__":
    preprocessor = TextPreprocessor()
    sample_text = "This is an example sentence for text preprocessing!"
    cleaned_text = preprocessor.clean_text(sample_text)
    print(f"Original: {sample_text}")
    print(f"Cleaned: {cleaned_text}")
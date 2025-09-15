# Data Preprocessing Process

The dataset [Best Books (10k) Multi-Genre Data](https://www.kaggle.com/datasets/ishikajohari/best-books-10k-multi-genre-data) was downloaded.
--

In `notebooks/eda/01_data_exploration.ipynb`, the data was processed as follows:
1. Missing values were replaced with empty strings ('').
2. Two new features were created: book title length and book description length.

The processed data was prepared for ML:
1. Data balancing was performed — all genres with fewer than 100 occurrences were excluded
2. A multi-dimensional binary vector was created using MultiLabelBinarizer, with a column for each genre containing 1 if the genre is present and 0 if not
3. The data was split into features and target variables
4. They were divided into training and testing subsets

Additionally, a function was created to preprocess the text itself (both separately and in columns) - converting to lowercase, removing special characters, removing stopwords, tokenizing and lemmatizing, followed by recombining tokens back into text.
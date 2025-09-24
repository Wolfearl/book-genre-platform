import pandas as pd
import joblib
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.multiclass import OneVsRestClassifier
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, HistGradientBoostingClassifier


# Uploading prepared data
print("Uploading data...")
multi_label_binarizer = joblib.load('../data/models/label_encoder.pkl')

data = joblib.load('../data/processed/train_test_split.pkl')
X_train = data['X_train']
X_test = data['X_test']
y_train = data['y_train']
y_test = data['y_test']

print(f"Training sample size: {X_train.shape}")
print(f"Test sample size: {X_test.shape}")

# Creating a converter for text and numeric attributes
text_features = ['Book', 'Description']
numeric_features = ['Title_Length', 'Description_Length', 'Avg_Rating']
preprocessor = ColumnTransformer(
    transformers=[
        ('title_tfidf', TfidfVectorizer(max_features=5000, ngram_range=(1, 2)), text_features[0]),
        ('desc_tfidf', TfidfVectorizer(max_features=5000, ngram_range=(1, 2)), text_features[1]),
        ('num', MinMaxScaler(), numeric_features)
    ],
    sparse_threshold=0
)

# Function for training and evaluating the model
def train_and_evaluate_model(model, model_name, X_train, y_train, X_test, y_test):
    """
    Train and evaluate a machine learning model using a pipeline with preprocessing.

    :param model: the machine learning model (estimator) to be trained
    :type model: sklearn.base.BaseEstimator
    :param model_name: a string representing the name of the model, used for printing status
    :type model_name: str
    :param X_train: training feature data
    :type X_train: pandas.DataFrame or numpy.ndarray
    :param y_train: training target labels
    :type y_train: pandas.Series or numpy.ndarray
    :param X_test: test feature data
    :type X_test: pandas.DataFrame or numpy.ndarray
    :param y_test: test target labels
    :type y_test: pandas.Series or numpy.ndarray
    :return: a tuple containing the trained pipeline and the accuracy score on the test data
    :rtype: tuple[sklearn.pipeline.Pipeline, float]
    """
    print(f"\n=== Model training: {model_name} ===")

    # Creating a pipeline
    pipeline = Pipeline([
        ('preprocessor', preprocessor),
        ('classifier', model)
    ], verbose=True)

    # Model training
    pipeline.fit(X_train, y_train)

    # Prediction based on test data
    y_pred = pipeline.predict(X_test)

    # Quality assessment
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.4f}")

    # Detailed classification report
    print("\nClassification Report:")
    print(classification_report(y_test.to_numpy(), y_pred, target_names=multi_label_binarizer.classes_,
                                zero_division=0))

    return pipeline, accuracy


# Initializing models
models = {
    'Naive Bayes': OneVsRestClassifier(MultinomialNB()),
    'Logistic Regression': OneVsRestClassifier(LogisticRegression(max_iter=1000, random_state=42, verbose=1)),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42, verbose=1),
    'Gradient Boosting': OneVsRestClassifier(HistGradientBoostingClassifier(max_iter=100, random_state=42, verbose=1))
}

# Training and evaluation of all models
result = {}
best_accuracy = 0
best_model = None
best_pipline = None

for name, model in models.items():
    pipline, accuracy = train_and_evaluate_model(model, name, X_train, y_train, X_test, y_test)
    result[name] = accuracy

    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_model = name
        best_pipline = pipline

print("\n=== Model comparison ===")
for name, accuracy in result.items():
    print(f"{name}: {accuracy:.4f}")

print(f"\nBest model: {best_model} with precision {best_accuracy:.4f}")

# Cross-validation for the best
print(f"\n=== Cross-validation for {best_model} ===")

# Creating a pipeline for cross-validation
pipline_cv = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', models[best_model])
], verbose=True)

# Performing cross-validation
cv_scores = cross_val_score(pipline_cv, X_train, y_train, cv=5, scoring='accuracy')
print("Cross validation results:")
print(f"Average accuracy: {cv_scores.mean():.4f} (+/-{cv_scores.std() * 2:.4f})")
print(f"All ratings: {cv_scores}")

# Setting hyperparameters for a better model
print(f"\n=== Setting hyperparameters for {best_model} ===")

match best_model:
    case 'Random Forest':
        param_grid = {
            'classifier__n_estimators': [50, 100],
            'classifier__max_depth': [10, 20],
            'classifier__min_samples_split': [2, 5]
        }
    case 'Gradient Boosting':
        param_grid = {
            'classifier__estimator__max_iter': [50, 100],
            'classifier__estimator__learning_rate': [0.01, 0.1],
            'classifier__estimator__max_depth': [3, 5]
        }
    case 'Logistic Regression':
        param_grid = {
            'classifier__C': [0.1, 1, 10],
            'classifier__solver': ['liblinear', 'saga']
        }
    case _:
        param_grid = {}

if param_grid:
    grid_search = GridSearchCV(
        pipline_cv, param_grid, cv=2, scoring='accuracy', n_jobs=-1, verbose=2
    )
    grid_search.fit(X_train, y_train)
    print(f"Best parameters: {grid_search.best_params_}")
    print(f"Best accuracy: {grid_search.best_score_:.4f}")

    # Using the best model
    best_pipeline = grid_search.best_estimator_

# Saving the best
print("\n=== Saving the best model ===")

# Training on all data for the final model
final_pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', models[best_model])
])

# If you have set up hyperparameters, we use the best parameters
if 'grid_search' in locals():
    final_pipeline.set_params(**grid_search.best_params_)

# Training on all data
final_pipeline.fit(pd.concat([X_train, X_test]), pd.concat([y_train, y_test]))

# Saving the model
joblib.dump(final_pipeline, '../data/models/book_genre_classifier.pkl')
print("The model is saved as '../data/models/book_genre_classifier.pkl'")

# Testing the saved model
loaded_model = joblib.load('../data/models/book_genre_classifier.pkl')
test_pred = loaded_model.predict(X_test[:5])
print("\nTest predictions:")
for i, pred in enumerate(test_pred):
    print(f"Book {i + 1}: {multi_label_binarizer.inverse_transform(np.array([pred]))[0]}")


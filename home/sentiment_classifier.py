import joblib
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer

# Load the trained model
model_file_path = r'C:\Users\inesz\OneDrive\Desktop\memoire\home\sentiment-analyzer.pkl'
model = joblib.load(model_file_path)

# Load the TF-IDF vectorizer
vectorizer_file_path = r'C:\Users\inesz\OneDrive\Desktop\memoire\home\vectorizer.pkl'
vectorizer = joblib.load(vectorizer_file_path)

def classify_sentiment(text):
    # Transform the input text into a numerical feature vector
    text_vector = vectorizer.transform([text])

    # Perform classification
    label = model.predict(text_vector)[0]

    return label






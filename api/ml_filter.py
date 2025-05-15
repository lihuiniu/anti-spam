import pickle
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Dummy training data
training_texts = [
    "Buy now and save big",
    "Limited time offer",
    "Earn money fast",
    "This is not spam",
    "Hello friend, how are you?",
    "Your invoice is attached"
]
labels = [1, 1, 1, 0, 0, 0]  # 1 = spam, 0 = not spam

# Vectorizer and model training
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(training_texts)
model = MultinomialNB()
model.fit(X_train, labels)

def is_spam_ml(text: str) -> bool:
    X_test = vectorizer.transform([text])
    prediction = model.predict(X_test)
    return bool(prediction[0])

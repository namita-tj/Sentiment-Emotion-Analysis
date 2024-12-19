import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import pandas as pd

# Load your dataset
# Replace 'your_dataset.csv' with the path to your dataset file
df = pd.read_csv('spam.csv')

# Assuming your dataset has 'text' column for email text and 'label' column for spam or not spam
X = df['text'].values
y = df['label'].values

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a CountVectorizer to convert text into tokens/features
vectorizer = CountVectorizer()

# Fit and transform the training data
X_train_counts = vectorizer.fit_transform(X_train)

# Transform the testing data
X_test_counts = vectorizer.transform(X_test)

# Train a Naive Bayes classifier
clf = MultinomialNB()
clf.fit(X_train_counts, y_train)

# Make predictions on the testing data
predictions = clf.predict(X_test_counts)

# Calculate accuracy
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)

# Example of classifying a new email
new_email = ["Congratulations! You've won a prize!"]
new_email_counts = vectorizer.transform(new_email)
prediction = clf.predict(new_email_counts)
print("Prediction for new email:", "Spam" if prediction[0] == 1 else "Not Spam")

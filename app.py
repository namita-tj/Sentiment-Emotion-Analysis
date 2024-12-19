from transformers import pipeline

# Load pre-trained sentiment model
sentiment_model = pipeline("sentiment-analysis")

# Load pre-trained emotion detection model
emotion_model = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

# Test the models with sample text
sample_text = "I love this product! It's amazing."

print(sentiment_model(sample_text))  # Returns sentiment (positive/negative)
print(emotion_model(sample_text))   # Returns emotion (joy, anger, etc.)


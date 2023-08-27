import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import re
import nltk
stemmer = nltk.SnowballStemmer("english")
from nltk.corpus import stopwords
import string
stopword = set(stopwords.words("english"))
from joblib import dump, load
import streamlit as st
from PIL import Image, ImageDraw

# Read the data
df = pd.read_csv("twitter_data.csv")

# Define the labels
df['labels'] = df['class'].map({0:"Hate Speech Detected", 1:"Offensive language Detected", 2:"No hate speech detected"})
df = df[['tweet','labels']]

# Define the function to preprocess the input text
def clean(text):
    text = str(text).lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' %re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    text = [word for word in text.split(' ') if word not in stopword]
    text =" ".join(text)
    text = [stemmer.stem(word) for word in text.split(' ')]
    text =" ".join(text)
    return text

# Preprocess the tweets
df["tweet"] = df["tweet"].apply(clean)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df["tweet"], df["labels"], test_size=0.33, random_state=42)

# Define the CountVectorizer
cv = CountVectorizer()

# Fit and transform the training data
X_train = cv.fit_transform(X_train)

# Train the DecisionTreeClassifier model
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Dump the trained model
dump(clf, 'my_model.joblib')

# Load the trained model
clf = load('my_model.joblib')

# Define the Streamlit app
def main():
    st.set_page_config(
    page_title="The Truth Project",
    page_icon="Hello"
    )
    
    # Load the image
    img = Image.open('4.PNG')

    mask = Image.new('L', img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + img.size, fill=255)
    img.putalpha(mask)
    # Get input from user
    user_input = st.text_input("Enter a sentence:")

    if user_input:
        # Preprocess the input text
        processed_input = clean(user_input)

        # Use the trained model to predict the label
        X_test = cv.transform([processed_input])
        prediction = clf.predict(X_test)[0]

        # Show the prediction
        if prediction == "Hate Speech Detected":
            st.error(prediction)
        elif prediction == "Offensive language Detected":
            st.warning(prediction)
        else:
            st.success(prediction)

if __name__ == "__main__":
    main()

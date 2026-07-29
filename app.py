import streamlit as st
import joblib
import re
import string
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk

# Download NLTK resources (first run only)
nltk.download("stopwords")
nltk.download("wordnet")

# Load model
model = joblib.load("random_forest_phishing_model.pkl")
tfidf = joblib.load("tfidf_vectorizer.pkl")

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()


def clean_text(text):
    text = text.lower()

    text = BeautifulSoup(text, "html.parser").get_text()

    text = re.sub(r"http\S+|www\S+", " ", text)

    text = re.sub(r"\S+@\S+", " ", text)

    text = re.sub(r"\d+", " ", text)

    text = text.translate(str.maketrans("", "", string.punctuation))

    text = re.sub(r"\s+", " ", text).strip()

    words = text.split()

    words = [
        lemmatizer.lemmatize(word)
        for word in words
        if word not in stop_words
    ]

    return " ".join(words)


st.set_page_config(
    page_title="Phishing Email Detector",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ AI-Driven Phishing Email Detection")

st.write(
    "Detect whether an email is **Phishing** or **Legitimate** using Machine Learning."
)

email = st.text_area(
    "Paste Email Content",
    height=250
)

if st.button("Analyze Email"):

    if email.strip() == "":
        st.warning("Please enter an email.")
    else:

        cleaned = clean_text(email)

        vector = tfidf.transform([cleaned])

        prediction = model.predict(vector)[0]

        probability = model.predict_proba(vector)[0]

        confidence = max(probability) * 100

        if prediction == 1:
            st.error("🚨 Phishing Email Detected")
        else:
            st.success("✅ Legitimate Email")

        st.metric(
            "Confidence",
            f"{confidence:.2f}%"
        )

        st.subheader("Prediction Probabilities")

        st.write({
            "Legitimate": round(probability[0] * 100, 2),
            "Phishing": round(probability[1] * 100, 2)
        })
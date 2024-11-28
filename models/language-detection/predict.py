import pickle
from pathlib import Path
import re

# Define the version and base directory for model loading
__version__ = "0.1.0"
BASE_DIR = Path(__file__).resolve(strict=True).parent

# Load the trained machine learning model
with open(f"{BASE_DIR}/language-detection-{__version__}.pkl", "rb") as f:
    model = pickle.load(f)


# Function to preprocess input text by removing unwanted characters
def preprocess_text(text: str) -> str:
    """
    Function to preprocess input text by removing unwanted characters
    """
    text = re.sub(r'[!@#$(),\n"%^*?\:;~`0-9]', " ", text)
    text = re.sub(r"[\[\]]", " ", text)
    return text.lower()


# Define the list of language classes
classes = [
    "Arabic",
    "Danish",
    "Dutch",
    "English",
    "French",
    "German",
    "Greek",
    "Hindi",
    "Italian",
    "Kannada",
    "Malayalam",
    "Portuguese",
    "Russian",
    "Spanish",
    "Sweedish",
    "Tamil",
    "Turkish",
]

# Function to predict the language of the given text
def predict(data):
    """
    Function to predict the language of the given text
    """
    # Preprocess the input text
    cleaned_text = preprocess_text(data["text"])
    # Predict the language using the model
    pred = model.predict([cleaned_text])
    # Return the corresponding language class
    return classes[pred[0]]
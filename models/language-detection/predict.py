import pickle
from pathlib import Path
from preprocess import preprocess_text  # Import preprocessing function

# Define the version and base directory for model loading
__version__ = "0.1.0"
BASE_DIR = Path(__file__).resolve(strict=True).parent

# Load the trained machine learning model
with open(f"{BASE_DIR}/language-detection-{__version__}.pkl", "rb") as f:
    model = pickle.load(f)

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
def predict_language(text):
    # Preprocess the input text
    cleaned_text = preprocess_text(text)
    # Predict the language using the model
    pred = model.predict([cleaned_text])
    # Return the corresponding language class
    return classes[pred[0]]

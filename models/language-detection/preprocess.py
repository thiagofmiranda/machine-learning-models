import re

# Function to preprocess input text by removing unwanted characters
def preprocess_text(text):
    # Remove special characters, punctuation, and numbers
    text = re.sub(r'[!@#$(),\n"%^*?\:;~`0-9]', " ", text)
    # Remove square brackets
    text = re.sub(r"[\[\]]", " ", text)
    # Convert text to lowercase
    text = text.lower()
    return text

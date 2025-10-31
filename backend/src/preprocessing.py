"""
preprocessing.py
----------------
Text preprocessing module for Rephrasinator project.
Handles cleaning, contraction expansion, stopword removal, 
spelling correction, lemmatization, and emoji cleanup.
"""

import re
import string
import nltk
import contractions
import emoji
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Download NLTK resources
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('omw-1.4', quiet=True)

# Initialize tools
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def remove_emojis_newlines(text):
    text = emoji.replace_emoji(text, replace='')
    text = text.replace('\n', ' ').replace('\r', ' ')
    return text

def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def expand_contractions(text):
    return contractions.fix(text)

def correct_spelling(text):
    return str(TextBlob(text).correct())

def remove_stopwords(text):
    words = word_tokenize(text)
    filtered = [w for w in words if w.lower() not in stop_words]
    return ' '.join(filtered)

def lemmatize_text(text):
    tokens = word_tokenize(text)
    lemmas = [lemmatizer.lemmatize(t) for t in tokens]
    return ' '.join(lemmas)

def preprocess_text(text, remove_stops=False, spell_check=False):
    text = remove_emojis_newlines(text)
    text = expand_contractions(text)
    text = clean_text(text)
    
    if spell_check:
        text = correct_spelling(text)
        
    if remove_stops:
        text = remove_stopwords(text)
        
    text = lemmatize_text(text)
    return text


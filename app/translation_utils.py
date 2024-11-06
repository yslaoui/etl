# app/translation_utils.py
from langdetect import detect, LangDetectException
from app.cache import cache  # Assuming a cache setup using Redis
import json
import os
import re
import requests


# Load the mock translations JSON file at the start of the app
def load_mock_translations():
    file_path = os.path.join(os.path.dirname(__file__), "mock_translations.json")
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)
    
# Store mock translations in a global variable for easy access
mock_translations = load_mock_translations()


def detect_language(text: str) -> str:
    """Detects the language of the given text, or returns 'unknown' if detection fails."""
    try:
        return detect(text)
    except LangDetectException:
        return "unknown"

def translate_text(text: str) -> str:
    """Translate text using mock translations loaded from a JSON file."""
    return mock_translations.get(text, f"Translated {text}")


def get_from_cache(text: str):
    """Retrieves cached translation and converts it from JSON."""
    cached_data = cache.get(text)
    if cached_data:
        return json.loads(cached_data.decode("utf-8"))  # Decode from bytes and parse JSON
    return None


def save_to_cache(text: str, language: str, translation: str):
    """Saves the translation in the cache as a JSON string."""
    data = json.dumps({"language": language, "translation": translation})
    cache.set(text, data)
# app/translation_utils.py
from langdetect import detect, LangDetectException
from app.cache import cache  # Assuming a cache setup using Redis
import json
import re

 
def detect_language(text: str) -> str:
    """Detects the language of the given text with additional validation."""
    # Basic checks for nonsensical or repetitive inputs
    if len(text) < 3 or re.fullmatch(r'(.)\1*', text):  # Checks for very short or repetitive input like "aaa"
        return "unknown"
    
    try:
        return detect(text)
    except LangDetectException:
        return "unknown"

def translate_text(text: str) -> str:
    """Mocks translation by returning a pre-defined translation."""
    mock_translations = {
        "Bonjour": "Hello",
        "Hola": "Hello",
        "Hallo": "Hello"
    }
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
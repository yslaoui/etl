# app/cache.py
import redis


# Configure Redis connection
cache = redis.Redis(host="localhost", port=6379, db=0)


def get(text: str):
   """Get a cached translation if available."""
   cached_data = cache.get(text)
   if cached_data:
       return eval(cached_data.decode("utf-8"))  
   return None


def set(text: str, data: dict):
   """Cache the translation for future use."""
   cache.set(text, str(data))  



from pydantic import BaseModel
from typing import Optional

class TranslationRequest(BaseModel):
    text: str

class TranslationResponse(BaseModel):
    text: str
    language: str
    translation: str
    from_cache: bool = False

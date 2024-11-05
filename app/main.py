# app/main.py
from fastapi import FastAPI, Depends, HTTPException
from app.schemas import TranslationRequest, TranslationResponse
from app.translation_utils import detect_language, translate_text  # Assume these utilities exist
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import  get_db
from app.schemas import TranslationRequest, TranslationResponse
from contextlib import asynccontextmanager
from app.database import engine
from app.init_db import init_db
from app.models import Translation
from app.translation_utils import detect_language, translate_text, get_from_cache, save_to_cache


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db(engine)
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

@app.post("/translate", response_model=TranslationResponse)
async def translate(request: TranslationRequest, db: AsyncSession = Depends(get_db)):
   # Check cache first
   cached_translation = get_from_cache(request.text)
   if cached_translation:
       return TranslationResponse(
           text=request.text,
           language=cached_translation["language"],
           translation=cached_translation["translation"],
           from_cache=True,
       )


   # Detect language
   language = detect_language(request.text)
   if language == "en":  # Assuming English text doesn't need translation
       translation = request.text
   else:
       # Translate the text (mocked)
       translation = translate_text(request.text)


   # Store the translation in the database
   new_translation = Translation(text=request.text, language=language, translation=translation)
   db.add(new_translation)
   await db.commit()
   await db.refresh(new_translation)


   # Cache the result
   save_to_cache(request.text, language, translation)


   # Return the translation response
   return TranslationResponse(
       text=request.text,
       language=language,
       translation=translation,
       from_cache=False,
   )

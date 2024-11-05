# app/main.py
from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database import engine
from app.init_db import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db(engine)
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

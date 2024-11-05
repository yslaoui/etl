# app/main.py
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import init_db, get_db

app = FastAPI()

@app.on_event("startup")
async def startup():
    # Initialize database on app startup
    await init_db()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

@app.get("/test-db")
async def test_db(db: AsyncSession = Depends(get_db)):
    # Test database connection by querying translations (table must be empty initially)
    result = await db.execute("SELECT 1")
    return {"db_test": result.scalar()}

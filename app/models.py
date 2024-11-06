from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

Base = declarative_base()

class Translation(Base):
    __tablename__ = 'translations'

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    language = Column(String, nullable=False)
    translation = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

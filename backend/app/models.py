# app/models.py
from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    text = Column(Text)

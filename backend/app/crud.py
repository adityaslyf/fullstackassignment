# app/crud.py
from sqlalchemy.orm import Session
from app import models, schemas

def create_document(db: Session, filename: str, text: str):
    db_document = models.Document(filename=filename, text=text)
    db.add(db_document)
    db.commit()
    db.refresh(db_document)
    return db_document

def get_document(db: Session, document_id: int):
    return db.query(models.Document).filter(models.Document.id == document_id).first()

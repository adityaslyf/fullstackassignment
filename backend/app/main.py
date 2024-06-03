# app/main.py
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app import crud, models, schemas, database, utils
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    # Save PDF file locally or to cloud storage
    file_location = f"files/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    
    # Extract text from PDF
    text = utils.extract_text_from_pdf(file_location)

    # Save file information and text to the database
    db = SessionLocal()
    document = crud.create_document(db, file.filename, text)

    return JSONResponse(content={"filename": file.filename})

@app.post("/ask/")
async def ask_question(file_id: int, question: str):
    db = SessionLocal()
    document = crud.get_document(db, file_id)
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    
    answer = utils.process_question(document.text, question)
    return JSONResponse(content={"answer": answer})

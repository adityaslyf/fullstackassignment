# app/utils.py
import fitz  # PyMuPDF
from langchain import LLM, LlamaIndex

def extract_text_from_pdf(file_path: str) -> str:
    pdf_document = fitz.open(file_path)
    text = ""
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text += page.get_text()
    return text

def process_question(text: str, question: str) -> str:
    llm = LLM()
    index = LlamaIndex()
    response = llm.ask_question(index.create_index(text), question)
    return response

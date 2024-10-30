# api/main.py
# API FastAPI dla serwisu przetwarzania PDF

from fastapi import FastAPI, HTTPException
from modules.pdf_processing import extract_text_from_pdf
from modules.embedding import generate_embedding, index_embedding

app = FastAPI()

@app.post("/process-pdf/")
async def process_pdf(pdf_path: str):
    """
    Endpoint do przetwarzania PDF: ekstrakcja tekstu, generowanie embeddingów, indeksowanie.
    
    :param pdf_path: Ścieżka do pliku PDF
    :return: Informacja o sukcesie operacji
    """
    try:
        text = extract_text_from_pdf(pdf_path)
        embedding = generate_embedding(text)
        index_embedding(embedding)
        return {"message": "PDF processed and indexed successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




#TODO: change template
# api/main.py
# API FastAPI dla serwisu LLM
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from modules.quiz_generation_chain import generate_quiz

load_dotenv()

app = FastAPI()

@app.post("/generate-quiz/")
async def generate_quiz_endpoint(text: str):
    """
    Endpoint do generowania quizu na podstawie tekstu.
    
    :param text: Tekst źródłowy
    :return: Wygenerowany quiz
    """
    try:
        quiz = generate_quiz(text)
        return {"quiz": quiz}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



#TODO: change template
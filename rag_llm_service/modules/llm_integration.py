# modules/llm_integration.py
# Moduł do integracji z modelem LLM

import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_content(prompt):
    """
    Generuje treść na podstawie podanego prompta za pomocą LLM.
    
    :param prompt: Tekst zapytania
    :return: Wygenerowany tekst
    """
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=prompt,
        max_tokens=150,
        temperature=0.7
    )
    return response.choices[0].text.strip()



#TODO: change template
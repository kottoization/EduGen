# modules/quiz_generation_chain.py
# Moduł generowania quizu

from modules.llm_integration import generate_content

def generate_quiz(text):
    """
    Generuje quiz na podstawie podanego tekstu.
    
    :param text: Tekst źródłowy
    :return: Wygenerowany quiz
    """
    prompt = f"Generate a quiz based on the following text:\n\n{text}"
    return generate_content(prompt)



#TODO: change template
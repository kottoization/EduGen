# modules/summary_chain.py
# Moduł generowania podsumowania

from modules.llm_integration import generate_content

def generate_summary(text):
    """
    Generuje podsumowanie najważniejszych informacji z podanego tekstu.
    
    :param text: Tekst źródłowy
    :return: Wygenerowane podsumowanie
    """
    prompt = f"Summarize the following text, focusing on the most important concepts and details:\n\n{text}"
    return generate_content(prompt)



#TODO: change template
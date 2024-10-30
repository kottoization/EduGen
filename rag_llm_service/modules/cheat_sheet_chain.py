# modules/cheat_sheet_chain.py
# Moduł generowania ściągi (cheat sheet)

from modules.llm_integration import generate_content

def generate_cheat_sheet(text):
    """
    Generuje ściągę na podstawie podanego tekstu, z kluczowymi informacjami do zapamiętania.
    
    :param text: Tekst źródłowy
    :return: Wygenerowana ściąga
    """
    prompt = f"Create a concise cheat sheet containing the most important information from the following text:\n\n{text}"
    return generate_content(prompt)



#TODO: change template
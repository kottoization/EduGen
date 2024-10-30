# modules/pdf_processing.py
# Moduł przetwarzania PDF - ekstrakcja tekstu

import pdfplumber

def extract_text_from_pdf(pdf_path):
    """
    Ekstrakcja tekstu z pliku PDF.
    
    :param pdf_path: Ścieżka do pliku PDF
    :return: Złączony tekst z każdej strony PDF
    """
    with pdfplumber.open(pdf_path) as pdf:
        text = ''.join([page.extract_text() for page in pdf.pages if page.extract_text()])
    return text



#TODO: change template
# tests/test_pdf_processing.py
# Testy modułu przetwarzania PDF

import pytest
from modules.pdf_processing import extract_text_from_pdf

def test_extract_text_from_pdf():
    """
    Test funkcji extract_text_from_pdf.
    """
    pdf_path = "tests/sample.pdf"
    text = extract_text_from_pdf(pdf_path)
    assert text is not None



#TODO: change template
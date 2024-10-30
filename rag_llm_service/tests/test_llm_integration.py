# tests/test_llm_integration.py
# Testy modułu integracji z LLM

import pytest
from modules.llm_integration import generate_content

def test_generate_content():
    """
    Test funkcji generate_content.
    """
    prompt = "What is AI?"
    response = generate_content(prompt)
    assert response is not None



#TODO: change template
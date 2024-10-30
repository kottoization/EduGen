# tests/test_chains.py
# Testy dla łańcuchów generacji treści (quiz, plan nauki, podsumowanie, ściąga)

import pytest
from modules.quiz_generation_chain import generate_quiz
from modules.learning_plan_chain import generate_learning_plan
from modules.summary_chain import generate_summary
from modules.cheat_sheet_chain import generate_cheat_sheet

def test_generate_quiz():
    """
    Test funkcji generate_quiz.
    """
    text = "Artificial Intelligence is the simulation of human intelligence by machines."
    quiz = generate_quiz(text)
    assert quiz is not None

def test_generate_learning_plan():
    """
    Test funkcji generate_learning_plan.
    """
    test_results = "The user shows good understanding of AI fundamentals but lacks knowledge in deep learning."
    learning_plan = generate_learning_plan(test_results)
    assert learning_plan is not None

def test_generate_summary():
    """
    Test funkcji generate_summary.
    """
    text = "Artificial Intelligence is the simulation of human intelligence by machines. It encompasses a variety of techniques and technologies, including machine learning and deep learning."
    summary = generate_summary(text)
    assert summary is not None

def test_generate_cheat_sheet():
    """
    Test funkcji generate_cheat_sheet.
    """
    text = "Artificial Intelligence (AI) includes machine learning, neural networks, and other advanced techniques to simulate human-like behavior."
    cheat_sheet = generate_cheat_sheet(text)
    assert cheat_sheet is not None




#TODO: change template
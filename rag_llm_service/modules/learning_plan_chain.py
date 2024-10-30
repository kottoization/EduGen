# modules/learning_plan_chain.py
# Moduł generowania planu nauki

from modules.llm_integration import generate_content

def generate_learning_plan(test_results):
    """
    Generuje plan nauki na podstawie wyników testu użytkownika.
    
    :param test_results: Wyniki testu użytkownika
    :return: Wygenerowany plan nauki
    """
    prompt = f"Based on the following test results, generate a personalized learning plan:\n\n{test_results}"
    return generate_content(prompt)



#TODO: change template
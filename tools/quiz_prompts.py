from langchain_core.prompts import ChatPromptTemplate

def generate_topic_list_prompt(subject: str) -> ChatPromptTemplate:
    """
    Generates a prompt template to create a list of quiz topics.
    """
    messages = [
        ("system", """
        You are an AI language model assistant with expertise in educational content creation.
        Your task is to generate a concise list of core topics for a quiz based on a given subject.
        Ensure the list includes essential concepts and is structured logically.
        """),
        ("human", f"Based on the following subject, generate a list of topics for a quiz:\nSubject: {subject}")
    ]
    return ChatPromptTemplate.from_messages(messages)

def generate_questions_prompt(topic: str) -> ChatPromptTemplate:
    """
    Generates a prompt template to create multiple-choice quiz questions.
    """
    messages = [
        ("system", """
        You are an AI language model assistant with expertise in educational content creation.
        Your task is to generate a set of multiple-choice questions for a quiz based on a given topic.
        Assign difficulty levels: 1 for easy, 2 for medium, and 3 for advanced.
        Ensure the quiz can be completed in 5-10 minutes.
        Provide the output in the following format:
        1. Question: [Your question here]
        Difficulty: [1, 2, or 3]
        a) [Option A]
        b) [Option B]
        c) [Option C]
        d) [Option D]
        Correct Answer: [a, b, c, or d]
        """),
        ("human", f"Generate a set of multiple-choice questions for the following topic:\nTopic: {topic}")
    ]
    return ChatPromptTemplate.from_messages(messages)

def assess_knowledge_level_prompt(topic: str, score_percentage: float) -> ChatPromptTemplate:
    """
    Generates a prompt template to assess user's knowledge level based on quiz performance for a specific topic.
    """
    messages = [
        ("system", """
        You are an AI language model assistant with expertise in educational assessment.
        Your task is to evaluate a user's knowledge level based on their quiz score percentage for a specific topic.
        Provide a concise assessment and suggest the next steps for their learning journey.
        """),
        ("human", f"Assess the user's knowledge level for the following topic:\nTopic: {topic}\nScore Percentage: {score_percentage}")
    ]
    return ChatPromptTemplate.from_messages(messages)

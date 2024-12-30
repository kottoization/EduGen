from tools.quiz_prompts import (
    generate_topic_list_prompt,
    generate_questions_prompt,
    assess_knowledge_level_prompt,
)
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableParallel, RunnableLambda


def generate_quiz(subject: str):
    """
    Generates a quiz based on the provided subject using parallel chains.
    """
    try:
        # Initialize the ChatOpenAI model
        llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.1, verbose=True)

        # Generate topics
        print(f"Generating topics for subject: {subject}")
        topic_prompt = generate_topic_list_prompt(subject)
        try:
            topic_result = llm.invoke(topic_prompt.format_prompt(subject=subject))
            topics = topic_result.content.split("\n")
            print(f"Generated topics: {topics}")
        except Exception as e:
            raise ValueError(f"Error generating topics: {e}")

        # Generate questions for all topics in parallel
        print("Generating questions for all topics...")
        try:
            question_chain = RunnableLambda(
                lambda inputs: generate_questions_prompt(inputs["topic"]).format_prompt(topic=inputs["topic"])
            ) | llm

            questions = question_chain.batch([{"topic": topic} for topic in topics])
        except Exception as e:
            raise ValueError(f"Error generating questions: {e}")

        # Assemble the quiz interactively
        print("\nStarting the quiz...\n")
        user_scores = {topic: 0 for topic in topics}
        total_questions = 0

        for topic, question_set in zip(topics, questions):
            print(f"Topic: {topic}\n")
            question_texts = question_set.content.split("\n\n")
            for question in question_texts:
                print(question)
                user_answer = input("Your answer: ").strip().lower()

                # Assess the answer dynamically
                try:
                    correct_answer = question.split("Correct Answer: ")[-1].strip().lower()
                    if user_answer == correct_answer:
                        print("Correct!\n")
                        user_scores[topic] += 1
                    else:
                        print(f"Wrong! The correct answer is: {correct_answer}\n")
                except Exception as e:
                    print(f"Error parsing question or correct answer: {e}")

                total_questions += 1

        # Display final results
        print("\nFinal Results:")
        for topic, score in user_scores.items():
            percentage = (score / total_questions) * 100
            print(f"Topic: {topic} - Score: {score}/{total_questions} ({percentage:.2f}%)")

    except Exception as e:
        print(f"An error occurred while generating the quiz: {e}")

from dotenv import load_dotenv
from QuizModule.quiz_operations import generate_quiz
from langchain_openai import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

def chat_with_bot():
    """
    Allows the user to chat freely with the bot, maintaining a chat history.
    """
    try:
        model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.1, verbose=True)
        chat_history = []  # Store conversation history

        # Initial system message
        system_message = SystemMessage(content="You are a helpful AI assistant.")
        chat_history.append(system_message)

        print("You can now chat with the bot. Type 'exit' or 'q' to quit.")
        while True:
            query = input("You: ")
            if query.lower() in ["exit", "q"]:  # Allow 'exit' or 'q' to quit
                break

            chat_history.append(HumanMessage(content=query))  # Add user message
            response = model.invoke(chat_history)  # Get AI response
            print(f"AI: {response.content}")

            chat_history.append(AIMessage(content=response.content))  # Add AI message

        print("---- Message History ----")
        for msg in chat_history:
            print(msg.content)

    except Exception as e:
        print(f"An error occurred while chatting with the bot: {e}")


def main_menu():
    """
    Main menu for the application.
    """
    print("Select an option:")
    print("1. Chat with the bot (no articles required)")
    print("2. Generate a quiz")
    choice = input("Enter the number of your choice: ")

    if choice == "1":
        chat_with_bot()
    elif choice == "2":
        subject = input("Enter the subject for the quiz: ")
        generate_quiz(subject)
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()

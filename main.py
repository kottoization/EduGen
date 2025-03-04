from dotenv import load_dotenv
import os
from QuizModule.quiz_operations import generate_quiz, generate_learning_plan_from_quiz
from LearningPlanModule.learning_plan import LearningPlan
from langchain_community.chat_models import ChatOpenAI
from langchain.schema.messages import AIMessage, HumanMessage, SystemMessage
from DocumentModule.file_handler import save_uploaded_file
from DocumentModule.text_extractor import extract_text_and_images
from DocumentModule.embedding_manager import generate_embeddings
from DocumentModule.chroma_manager import initialize_chroma, embedding_exists, add_embedding

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

def upload_and_process_document():
    file_path = input("Type file path: ")
    text, images = extract_text_and_images(file_path)

    if not text:
        print("There was an error while extracting text from the file.")
        return

    texts, embeddings = generate_embeddings(text)

    if not texts or not embeddings:
        print("Failed to generate embeddings.")
        return

    chroma_client = initialize_chroma()
    added_chunks = 0
    skipped_chunks = 0

    for chunk_text, embedding in zip(texts, embeddings):
        metadata = {
            "source": file_path,
            "chunk_preview": chunk_text[:100]  # optional preview of the chunk
        }

        if not embedding_exists(chroma_client, embedding):
            add_embedding(chroma_client, chunk_text, embedding, metadata)
            added_chunks += 1
        else:
            skipped_chunks += 1

    print(f"Processing completed. Added {added_chunks} new chunks, skipped {skipped_chunks} duplicates.")



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
    while True:
        print("\nSelect an option:")
        print("1. Chat with the bot (no articles required)")
        print("2. Generate a quiz")
        print("3. Create a personalized learning plan")
        print("4. Upload and process document")
        print("5. Exit")
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            chat_with_bot()
        elif choice == "2":
            subject = input("Enter the subject for the quiz: ")
            generate_quiz(subject)
        elif choice == "3":
            print("\nSelect an option:")
            print("1. Take a quiz to generate a learning plan")
            print("2. Input custom learning goals")
            sub_choice = input("Enter your choice: ")

            if sub_choice == "1":
                subject = input("Enter the subject for the quiz: ")
                quiz_results = generate_quiz(subject)  # Generates quiz and returns results
                user_name = input("Enter your name: ")
                generate_learning_plan_from_quiz(user_name, quiz_results)
            elif sub_choice == "2":
                user_name = input("Enter your name: ")
                goals_input = input("Enter your learning goals (comma-separated): ")
                user_input = {
                    "goals": [goal.strip() for goal in goals_input.split(",")]
                }
                plan = LearningPlan(user_name=user_name)
                plan.generate_plan_from_prompt(user_input)
                plan.display_plan()
            else:
                print("Invalid choice. Please try again.")
        elif choice == "4":
            upload_and_process_document()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()

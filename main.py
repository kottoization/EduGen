from tools.prompts import instruction_str, prompt_template, context
from dotenv import load_dotenv
from llama_index.core.query_engine import PandasQueryEngine as pqe
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
from data_operations import load_articles_df
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

def query_agent(articles_df):
    '''
    The goal of this method is to create an PandasQueryEngine agent that will allow the user to chat with LLM chatbot.
    '''
    if articles_df is not None:
        try:
            articles_query_engine = pqe(df=articles_df, verbose=True, instruction_str=instruction_str)
            articles_query_engine.update_prompts({"pandas_prompt": prompt_template})

            articles_metadata = ToolMetadata(
                name="articles_data",
                description=(
                    "this gives information about facts from Medium articles."
                    "Use a detailed plain text question as input to the tool."
                ),
            )

            query_engine_tools = [
                QueryEngineTool(
                    query_engine=articles_query_engine,
                    metadata=articles_metadata,
                ),
            ]
            llm = OpenAI(model="gpt-4", temperature=0.1)

            agent = ReActAgent.from_tools(query_engine_tools, llm=llm, verbose=True, context=context)

            while (prompt := input("Enter a prompt (q to quit): ")) != "q":
                result = agent.query(prompt)
                print(result)
        except Exception as e:
            print(f"An error occurred while running the query agent: {str(e)}")
    else:
        print("No data to query.")

if __name__ == "__main__":
    articles_df = load_articles_df()
    query_agent(articles_df)
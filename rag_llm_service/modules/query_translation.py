from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from operator import itemgetter
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnablePassthrough
from langchain.load import dumps, loads

#TODO: change template -> think of what do I really need it to 

#comments: will probably be useful for notes generation, summary generation, cheat sheets generation ect

def needs_changes_multi_query(user_query: str):
    """You are an AI language model assistant. Your task is to generate five 
    different versions of the given user question to retrieve relevant documents from a vector 
    database. By generating multiple perspectives on the user question, your goal is to help
    the user overcome some of the limitations of the distance-based similarity search. 
    Provide these alternative questions separated by newlines. Original question: {question}"""

    generate_queries = (
    prompt_perspectives 
    | ChatOpenAI(temperature=0) 
    | StrOutputParser() 
    | (lambda x: x.split("\n"))
    )

    return generate_queries


def needs_changes_get_unique_union(documents: list[list]):
    """ Unique union of retrieved docs """
    # Flatten list of lists, and convert each Document to string
    flattened_docs = [dumps(doc) for sublist in documents for doc in sublist]
    # Get unique documents
    unique_docs = list(set(flattened_docs))
    # Return
    return [loads(doc) for doc in unique_docs]


def needs_changes_generate_multi_query_different_perspectives(user_query: str):    
    #TODO: ADD whatss below in order for it to work
    
    # Index
    #from langchain_openai import OpenAIEmbeddings
    #from langchain_community.vectorstores import Chroma
    #vectorstore = Chroma.from_documents(documents=splits, 
    #                               embedding=OpenAIEmbeddings())

    #aretriever = vectorstore.as_retriever()

    retrieval_chain = multi_query | retriever.map() | get_unique_union

    #docs = retrieval_chain.invoke({"question":user_query})

    template = """Answer the following question based on this context:

    {context}

    Question: {question}
    """

    prompt = ChatPromptTemplate.from_template(template)

    #TODO:  change
    llm = ChatOpenAI(temperature=0)

    final_rag_chain = (
        {"context": retrieval_chain, 
        "question": itemgetter("question")} 
        | prompt
        | llm
        | StrOutputParser()
    )

    final_rag_chain.invoke({"question":user_query})

    #return TODO: ADD THIS



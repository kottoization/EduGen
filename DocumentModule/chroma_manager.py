from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

def initialize_chroma(persist_directory='chroma_db', collection_name='documents'):
    embedding_function = OpenAIEmbeddings()
    return Chroma(
        collection_name=collection_name,
        persist_directory=persist_directory,
        embedding_function=embedding_function
    )

def embedding_exists(chroma_client, embedding, threshold=0.95):
    results = chroma_client.similarity_search_by_vector(embedding, k=1)
    return len(results) > 0

def add_embedding(chroma_client, chunk_text, embedding, metadata):
    chroma_client.add_texts(
        texts=[chunk_text], 
        metadatas=[metadata],
        embeddings=[embedding]
    )
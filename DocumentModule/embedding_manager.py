from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

#TODO: adjust chunk size later on, also perhaps adding more splitting techniques would be benefitial
def generate_embeddings(text, model_name="text-embedding-3-large", chunk_size=4500, chunk_overlap=200):
    try:
        # Initialize the text splitter
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )
        # Split the text into manageable chunks
        texts = text_splitter.split_text(text)

        if not texts: 
            print("No text chunks were created.")
            return [], [] 
        
        # Initialize the embeddings model
        embeddings = OpenAIEmbeddings(model=model_name)
        
        # Generate embeddings for each chunk
        embeddings_list = embeddings.embed_documents(texts)
        
        return texts, embeddings_list
    except Exception as e:
        print(f"An error occurred while generating embeddings: {str(e)}")
        return [], []
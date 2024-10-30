# modules/embedding.py
# Moduł do generowania embeddingów i indeksowania

from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def generate_embedding(text):
    """
    Generuje embedding dla podanego tekstu.
    
    :param text: Tekst do embeddingu
    :return: Wektor embeddingowy
    """
    return model.encode(text)

def index_embedding(embedding):
    """
    Indeksuje embedding za pomocą Pinecone/Faiss.
    
    :param embedding: Wektor embeddingowy
    """
    # TODO: Dodaj implementację indeksowania
    pass



#TODO: change template
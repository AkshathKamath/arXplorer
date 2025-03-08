import pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from config import PINECONE_API_KEY, PINECONE_ENVIRONMENT

# Initialize Pinecone
pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENVIRONMENT)
index_name = "arxiv-papers"

if index_name not in pinecone.list_indexes():
    pinecone.create_index(index_name, dimension=1536, metric="cosine")

index = pinecone.Index(index_name)
embeddings = OpenAIEmbeddings()

def store_paper_in_pinecone(paper_id, text, paper_url):
    """Stores paper embeddings in Pinecone."""
    embedding = embeddings.embed_query(text[:5000])  # Limit to avoid token constraints
    index.upsert([(paper_id, embedding, {"text": text[:5000], "url": paper_url})])

    return {"message": "Paper stored successfully", "paper_id": paper_id}
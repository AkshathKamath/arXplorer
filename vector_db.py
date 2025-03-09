from pinecone import Pinecone
from sentence_transformers import SentenceTransformer
#from config import PINECONE_API_KEY, PINECONE_ENVIRONMENT
import redis
import hashlib

# Initialize Redis client
redis_client = redis.Redis(host="localhost", port=6379, db=0)

# Initialize Pinecone
pc = Pinecone(api_key="pcsk_6PUmzH_58RKsC3EDHpGHL5nFX6dfNfRBZz9vQKzYKUfjrQSJcSU4m8CQxkZnjsKdqw6FEf")
index_name = "paper-summarizer"

index = pc.Index(index_name)

# Initialize Sentence Transformers model
model = SentenceTransformer('all-MiniLM-L6-v2')

# generate unique id for reserach paper
def generate_id_from_text(text):
    return hashlib.md5(text.encode()).hexdigest()

def process_text_to_embeddings(text):
    embeddings = model.encode(text)
    return embeddings


# Upsert embeddings into Pinecone
def store_embeddings_in_pinecone(paper_id, embeddings):
    index.upsert([(paper_id, embeddings)])

def main():
    text = redis_client.get("extracted_text")
    if not text:
        print("No text found in Redis.")
        return

    text = text.decode("utf-8")

    paper_id = generate_id_from_text(text)

    # Example metadata (replace this with actual metadata from your FastAPI app)
    # metadata = {
    #     "title": "Example Paper Title",  # Replace with actual title
    #     "url": "http://example.com/paper.pdf",  # Replace with actual URL
    #     "text": text  # Optional: Store the full text
    # }

    embeddings = process_text_to_embeddings(text)
    store_embeddings_in_pinecone(paper_id, embeddings)
    print(f"Embeddings for paper {paper_id} stored in Pinecone with metadata.")

if __name__ == "__main__":
    main()
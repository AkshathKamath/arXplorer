import pinecone
import json
from langchain.embeddings.openai import OpenAIEmbeddings

pinecone.init(api_key="pcsk_6PUmzH_58RKsC3EDHpGHL5nFX6dfNfRBZz9vQKzYKUfjrQSJcSU4m8CQxkZnjsKdqw6FEf", environment="us-east1-aws")

index_name = "arxiv-papers"

if index_name not in pinecone.list_indexes():
    pinecone.create_index(index_name, dimension=1536, metric="cosine")

index = pinecone.Index(index_name)
embeddings = OpenAIEmbeddings()

def store_papers():
    """Store extracted papers in Pinecone."""
    with open("papers.json", "r") as f:
        papers = json.load(f)

    for paper in papers:
        embedding = embeddings.embed_query(paper["title"] + " " + paper["abstract"])
        index.upsert([(paper["id"], embedding, {"title": paper["title"], "abstract": paper["abstract"]})])

if __name__ == "__main__":
    store_papers()
    print("Papers stored in Pinecone!")
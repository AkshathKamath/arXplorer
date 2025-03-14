from langchain.vectorstores import Pinecone
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone as PineconeClient
import os

embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

pc = PineconeClient(api_key="pcsk_6PUmzH_58RKsC3EDHpGHL5nFX6dfNfRBZz9vQKzYKUfjrQSJcSU4m8CQxkZnjsKdqw6FEf") # Store API key in env variable
index_name = "paper-summarizer"
index = pc.Index(index_name)

def embed_query(query):
    return embedding_model.encode(query).tolist()

vector_store = Pinecone(index, embed_query, "text")

# retriever for fetching relevant documents
retriever = vector_store.as_retriever(search_kwargs={"k": 5})  

llm = ChatOpenAI(model_name="gpt-4", temperature=0)
qa_chain = RetrievalQA.from_chain_type(llm, retriever=retriever, return_source_documents=True)

def answer_question(query):
    response = qa_chain(query)
    answer = response["result"]
    sources = [doc.metadata["text"] for doc in response["source_documents"]]
    
    return {"answer": answer, "sources": sources}


# Example usage
query = "What is RAG?"
result = answer_question(query)
print("Answer:", result["answer"])
print("Sources:", result["sources"])
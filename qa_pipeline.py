# from sentence_transformers import SentenceTransformer
from pinecone import Pinecone
from llama_index.core import VectorStoreIndex, ServiceContext, StorageContext
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.vector_stores.pinecone import PineconeVectorStore
# from llama_index.llms.openai import OpenAI
from llama_index.llms.mistralai import MistralAI


pc = Pinecone(api_key="pcsk_6PUmzH_58RKsC3EDHpGHL5nFX6dfNfRBZz9vQKzYKUfjrQSJcSU4m8CQxkZnjsKdqw6FEf")
index_name = "paper-summarizer"
index = pc.Index(index_name)


vector_store = PineconeVectorStore(pc.Index(index_name))
storage_context = StorageContext.from_defaults(vector_store=vector_store)
llm = MistralAI(model="mistral-7b", api_key = "OAaFT0jM8jGshHiF2jUste5tX61rTSOP")


embedding_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")
service_context = ServiceContext.from_defaults(llm=llm, embed_model=embedding_model)

index = VectorStoreIndex.from_vector_store(vector_store, storage_context=storage_context)


query_engine = index.as_query_engine(service_context=service_context, similarity_top_k=5)

# Function to answer questions
def answer_question(query):
    response = query_engine.query(query)
    return {"answer": response.response, "sources": response.source_nodes}


query = "What is RAG?"
result = answer_question(query)
print("Answer:", result["answer"])
print("Sources:", result["sources"])
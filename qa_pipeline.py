from langchain.vectorstores import Pinecone
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from vector_db import index, embeddings

llm = ChatOpenAI(model_name="gpt-4", temperature=0)
vector_store = Pinecone(index, embeddings.embed_query, "text")
retriever = vector_store.as_retriever()
qa_chain = RetrievalQA.from_chain_type(llm, retriever=retriever)

def answer_question(query):
    """Retrieves relevant papers and answers user queries."""
    return qa_chain.run(query)
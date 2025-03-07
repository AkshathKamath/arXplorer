from fastapi import FastAPI, HTTPException, Request
import uvicorn
import pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI

app = FastAPI()

pinecone.init(api_key="pcsk_6PUmzH_58RKsC3EDHpGHL5nFX6dfNfRBZz9vQKzYKUfjrQSJcSU4m8CQxkZnjsKdqw6FEf", environment="us-east1-aws")
index = pinecone.Index("arxiv-papers")
embeddings = OpenAIEmbeddings()

""" this we can modify later based on usecase"""
llm = OpenAI(model_name="gpt-4", api_key="YOUR_OPENAI_API_KEY")

@app.post("/ask/")
async def ask_question(request: Request):
    """Retrieve relevant papers and answer questions."""
    try:
        body = await request.json()
        query = body.get("query")

        if not query:
            raise HTTPException(status_code=400, detail="Missing 'query' in request body")

        # Step 1: Embed user query
        query_embedding = embeddings.embed_query(query)

        # Step 2: Retrieve relevant papers from Pinecone
        results = index.query(query_embedding, top_k=3, include_metadata=True)
        retrieved_papers = [res["metadata"]["abstract"] for res in results["matches"]]

        # Step 3: Generate answer using LLM
        context = " ".join(retrieved_papers)
        prompt = f"Context: {context}\nQuestion: {query}\nAnswer:"
        answer = llm(prompt)

        return {"answer": answer}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=5000)
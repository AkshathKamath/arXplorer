from fastapi import FastAPI, HTTPException, Request
import uvicorn
import httpx
import xml.etree.ElementTree as ET
from pinecone import Pinecone
from sentence_transformers import SentenceTransformer
import hashlib
from textwrap import wrap

app = FastAPI()

pc = Pinecone(api_key="pcsk_6PUmzH_58RKsC3EDHpGHL5nFX6dfNfRBZz9vQKzYKUfjrQSJcSU4m8CQxkZnjsKdqw6FEf")
index_name = "paper-summarizer"

index = pc.Index(index_name)
model = SentenceTransformer('all-MiniLM-L6-v2')

def generate_id_from_text(text):
    return hashlib.md5(text.encode()).hexdigest()

def process_text_to_embeddings(text):
    chunks = wrap(text, width=512)  
    embeddings = [model.encode(chunk) for chunk in chunks]
    return embeddings

def store_embeddings_in_pinecone(paper_id, embeddings, chunks):
    vectors = []
    for i, embedding in enumerate(embeddings):
        chunk_id = f"{paper_id}_{i}"  
        metadata = {"text": chunks[i]}  
        vectors.append((chunk_id, embedding, metadata))

    index.upsert(vectors)  

@app.get('/') 
def home_route():
    return {"msg":"This route works!"}

@app.post('/store_to_pinecone/')
async def pinecone_upload(request: Request):
    try:
        body = await request.json()
        async with httpx.AsyncClient() as client:
            response = await client.post("https://arxplorer-production.up.railway.app/extract_pdf_text/", json=body)

        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Failed to extract text from PDF")

        text = response.json().get("text", "")
        print(text)

        paper_id = generate_id_from_text(text)
        # embeddings = process_text_to_embeddings(text)
        # store_embeddings_in_pinecone(paper_id, embeddings)
        chunks = wrap(text, width=512)  # Split text into chunks
        embeddings = process_text_to_embeddings(text)  # Encode chunks
        store_embeddings_in_pinecone(paper_id, embeddings, chunks)  # Store properly

        return {"message": f"Embeddings for paper {paper_id} stored in Pinecone."}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == '__main__':
	uvicorn.run(app, host='0.0.0.0', port=4000)
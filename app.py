from fastapi import FastAPI, HTTPException, Request
import uvicorn
import httpx
import json
import xml.etree.ElementTree as ET
import fitz 
import io
import redis

# Initialize Redis client
redis_client = redis.Redis(host="localhost", port=6379, db=0)

app = FastAPI()

ARXIV_API_URL = "http://export.arxiv.org/api/query"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

@app.get('/') 
def home_route():
    return {"msg":"This route works!"}

@app.post("/search_papers/")
async def search_papers(request: Request):
    try:
        body = await request.json()  # Read JSON payload
        title = body.get("title")

        if not title:
            raise HTTPException(status_code=400, detail="Missing 'title' in request body")

        query = f"all:{title.replace(' ', '+')}"
        url = f"{ARXIV_API_URL}?search_query={query}&start=0&max_results=10"

        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=HEADERS)

        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Failed to fetch data from arXiv")

        root = ET.fromstring(response.text)
        ns = {'ns': 'http://www.w3.org/2005/Atom'}

        papers = []
        for entry in root.findall("ns:entry", ns)[:5]:
            paper_title = entry.find("ns:title", ns).text.strip()
            link = entry.find("ns:id", ns).text.strip()

            paper_id = link.split("/")[-1]  
            link = f"http://export.arxiv.org/pdf/{paper_id}.pdf"
            
            papers.append({"title": paper_title, "link": link})

        return {"papers": papers}

    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON payload")
    
@app.post("/extract_pdf_text/")
async def extract_pdf_text(request: Request):
    try:
        body = await request.json()
        print("Request body:", body)  # Debug: Print the request body
        paper_url = body.get("url")

        if not paper_url:
            raise HTTPException(status_code=400, detail="Missing 'url' in request body")

        # Ensure URL is a PDF
        if not paper_url.endswith(".pdf"):
            raise HTTPException(status_code=400, detail="Provided URL is not a PDF")

        # Debug: Print the PDF URL
        print("Downloading PDF from:", paper_url)

        # Download the PDF file
        async with httpx.AsyncClient() as client:
            response = await client.get(paper_url)
            print("PDF download status code:", response.status_code)  # Debug: Print status code

        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Failed to fetch the PDF file")

        # Debug: Print the first 100 bytes of the PDF
        print("PDF content (first 100 bytes):", response.content[:100])

        # Extract text using PyMuPDF
        pdf_text = extract_text_from_pdf(response.content)

        # Debug: Print the first 100 characters of the extracted text
        print("Extracted text (first 100 characters):", pdf_text[:100])

        # Push the extracted text to Redis
        redis_client.set("extracted_text", pdf_text)

        return {"text": pdf_text}

    except Exception as e:
        print("Error:", str(e))  # Debug: Print the exception
        raise HTTPException(status_code=500, detail=str(e))

def extract_text_from_pdf(pdf_bytes):
    """Extract text from a PDF file using PyMuPDF."""
    text = ""
    with fitz.open("pdf", pdf_bytes) as pdf:
        for page in pdf:
            text += page.get_text("text") + "\n\n"
    return text.strip()

if __name__ == '__main__':
	uvicorn.run(app, host='0.0.0.0', port=4000)
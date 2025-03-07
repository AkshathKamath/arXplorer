from fastapi import FastAPI, HTTPException, Request
import uvicorn
import httpx
import json
import xml.etree.ElementTree as ET

app = FastAPI()

ARXIV_API_URL = "http://export.arxiv.org/api/query"

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
            response = await client.get(url)

        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Failed to fetch data from arXiv")

        root = ET.fromstring(response.text)
        ns = {'ns': 'http://www.w3.org/2005/Atom'}

        papers = []
        for entry in root.findall("ns:entry", ns)[:5]:
            paper_title = entry.find("ns:title", ns).text.strip()
            link = entry.find("ns:id", ns).text.strip()
            link = link.replace("abs", "pdf") + ".pdf"
            
            papers.append({"title": paper_title, "link": link})

        return {"papers": papers}

    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON payload")

if __name__ == '__main__':
	uvicorn.run(app, host='0.0.0.0', port=4000)
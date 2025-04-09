from fastapi import FastAPI, HTTPException, Request
import uvicorn
import httpx
from summarize import summarize_text 

app = FastAPI()

@app.get('/') 
def home_route():
    return {"msg":"This route works!"}

@app.post('/summarize_paper/')
async def summarize_paper(request: Request):
    try:
        body = await request.json()
        async with httpx.AsyncClient() as client:
            response = await client.post("https://arxplorer-production.up.railway.app/extract_pdf_text/", json=body)
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Failed to extract text from PDF")
        
        text = response.json().get("text", "")
        if not text:
            raise HTTPException(status_code=500, detail="No text extracted from PDF")
        
        summary = summarize_text(text)

        return {"summary": summary}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
      
if __name__ == '__main__':
	uvicorn.run(app, host='0.0.0.0', port=4200)
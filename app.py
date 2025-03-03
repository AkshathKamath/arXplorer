from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.get('/') 
def home_route():
    return {"msg":"This route works!"}

if __name__ == '__main__':
	uvicorn.run(app, host='0.0.0.0', port=4000)
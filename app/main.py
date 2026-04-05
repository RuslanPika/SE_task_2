from fastapi import FastAPI
from app.schemas import RequestData, ResponseData
from app.model import generate_response

app = FastAPI(title="LLM API")

@app.get("/")
def root():
    return {"message": "API is working"}

@app.post("/generate", response_model=ResponseData)
def generate(data: RequestData):
    result = generate_response(data.prompt)
    return {"response": result}
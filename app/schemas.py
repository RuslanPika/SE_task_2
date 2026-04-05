from pydantic import BaseModel

class RequestData(BaseModel):
    prompt: str

class ResponseData(BaseModel):
    response: str
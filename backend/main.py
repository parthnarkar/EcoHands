from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class URLInput(BaseModel):
    url: str

@app.post("/extract-article")
def extract_article(input_data : URLInput):
    return {"received_url": input_data.url}

@app.get("/")
def root():
    return {"message": "FastAPI is working!"}


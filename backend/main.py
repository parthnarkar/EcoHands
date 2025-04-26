from fastapi import FastAPI
from pydantic import BaseModel
from scraper import extract_article
from summarizer import summarize_text

app = FastAPI()

class URLInput(BaseModel):
    url: str

@app.post("/extract-article")
def extract_and_summarize(input_data: URLInput):
    # Step 1: Extract article
    article_data = extract_article(input_data.url)

    # If extraction failed, return the error
    if "error" in article_data:
        return {"error": article_data["error"]}
    
    # Step 2: Summarize the article text
    summary = summarize_text(article_data["text"])

    # Step 3: Return full result
    return {
        "title": article_data["title"],
        "date": article_data["date"],
        "authors": article_data["authors"],
        "original_text_snippet": article_data["text"][:300],  # Optional: show only snippet
        "summary": summary
    }

@app.get("/")
def root():
    return {"message": "FastAPI is working!"}

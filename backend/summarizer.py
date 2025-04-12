from transformers import pipeline
import re

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def extract_keywords(text: str, top_k: int = 10) -> list:
    """
    Simple keyword extractor using word frequency (excluding stop words).
    """
    stop_words = set([
        "the", "and", "to", "of", "in", "a", "on", "for", "with", "we", "our",
        "is", "was", "that", "as", "at", "be", "by", "an", "are", "from", "this",
        "it", "or", "which", "they", "their"
    ])
    
    words = re.findall(r'\b[a-zA-Z]{4,}\b', text.lower())  # only words with 4+ letters
    freq = {}
    for word in words:
        if word not in stop_words:
            freq[word] = freq.get(word, 0) + 1
    keywords = sorted(freq, key=freq.get, reverse=True)
    return keywords[:top_k]

def summarize_text(text: str) -> str:
    if not text:
        return "No input text provided."
    
    try:
        # Limit input text to 1500 characters
        text = text[:1500]
        
        # Generate summary using the model
        summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
        final_summary = summary[0]['summary_text']

        # Validate presence of key terms
        validated_summary = validate_summary(final_summary, text)
        
        return validated_summary
    
    except Exception as e:
        return f"Summarization failed: {str(e)}"

def validate_summary(summary: str, original_text: str) -> str:
    """
    Ensure summary contains important keywords from original text.
    """
    key_terms = extract_keywords(original_text)
    missing = [kw for kw in key_terms if kw not in summary.lower()]
    
    if missing:
        print(f"⚠️ Warning: Summary might be missing keywords: {missing}")
    
    return summary

if __name__ == "__main__":
    sample_text = """
        In their letter, Padilla and Welch requested information about the companies’ current and previous safety measures and any research on the efficacy of those measures, as well as the names of safety leadership and well-being practices in place for safety teams. They also asked the firms to describe the data used to train their AI models and how it “influences the likelihood of users encountering age-inappropriate or other sensitive themes.”
    """
    
    print("🧠 Summary:")
    print(summarize_text(sample_text))

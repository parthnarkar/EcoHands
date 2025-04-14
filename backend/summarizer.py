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
        original_text = text[:1500]
        
        # Extract keywords and build a soft guiding prompt
        key_terms = extract_keywords(original_text)
        keyword_prompt = ", ".join(key_terms)

        guided_prompt = (
            f"Please summarize the following text, making sure to highlight all the key points and including important details such as {keyword_prompt}. "
            "Ensure that the summary provides an accurate and concise representation of the main ideas, including the most relevant terms and topics from the original text:\n\n"
            f"{original_text}"
        )
        
        # Generate summary
        summary = summarizer(guided_prompt, max_length=150, min_length=40, do_sample=False)
        final_summary = summary[0]['summary_text']

        # Check for missing important keywords (optional, for dev/debugging)
        validated_summary = validate_summary(final_summary, original_text)
        
        return validated_summary

    except Exception as e:
        return f"Summarization failed: {str(e)}"

def validate_summary(summary: str, original_text: str) -> str:
    """
    Print a warning if important keywords from original text are missing.
    """
    key_terms = extract_keywords(original_text)
    missing = [kw for kw in key_terms if kw not in summary.lower()]
    
    if missing:
        print(f"⚠️ Warning: Summary might be missing keywords: {missing}")
    
    return summary

if __name__ == "__main__":
    sample_text = """
        The European Union has announced a sweeping set of AI regulations aimed at safeguarding public interest while fostering innovation.
        The new laws will categorize AI systems into different levels of risk — from minimal to unacceptable — and will impose strict rules on high-risk applications, including biometric surveillance and algorithmic decision-making in hiring.
        Under the new guidelines, companies developing or deploying AI systems in the EU must be transparent about how their algorithms function, including documentation on datasets used, accuracy levels, and safety checks.
        The legislation comes in response to growing concerns over the ethical use of artificial intelligence and fears about biased decision-making, job displacement, and privacy violations.
        European Commission President Ursula von der Leyen stated that the rules aim to ensure Europe remains a global leader in trustworthy AI.
        The proposal still needs approval from member states and the European Parliament, but it's already being hailed as a landmark step in regulating emerging technologies.
        Meanwhile, tech companies are responding cautiously. Some have welcomed the move for more clarity, while others warn the rules could stifle innovation and raise compliance costs.
    """
    
    print("🧠 Summary:")
    print(summarize_text(sample_text))
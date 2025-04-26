from transformers import pipeline

# Use a lighter, faster model
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(text: str) -> str:
    """
    Summarize the given text into a concise and meaningful summary.
    """
    if not text:
        return "No input text provided."
    
    try:
        # Limit input text to 1500 characters (safe for summarizer)
        original_text = text[:1500]

        # Directly summarize without keyword prompt
        summary = summarizer(original_text, max_length=150, min_length=40, do_sample=False)

        # Extract the text from the output
        final_summary = summary[0]['summary_text']

        return final_summary

    except Exception as e:
        return f"Summarization failed: {str(e)}"

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
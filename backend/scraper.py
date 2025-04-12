from newspaper import Article

def extract_article(url: str) -> dict:
    """
    Extracts title, text, publish date, and authors from a news article URL.

    Args:
        url (str): The URL of the news article.

    Returns:
        dict: Dictionary containing article data or an error message.
    """

    try:
        article = Article(url)
        article.download()
        article.parse()

        return {
            "title": article.title,
            "text": article.text,
            "date": str(article.publish_date) if article.publish_date else "Unknown",
            "authors": article.authors
        }
    
    except Exception as e:
        return{
            "error": f"Failed to extract article: {str(e)}"
        }

if __name__ == "__main__":
    test_url = "https://edition.cnn.com/2025/04/11/americas/trump-china-trade-war-allies-intl-latam/index.html"
    result = extract_article(test_url)

    if "error" in result:
        print("❌ Error:", result["error"])
    else:
        print("✅ Title:", result["title"])
        print("📝 Text Snippet:", result["text"][:300], "...")
        print("📅 Date:", result["date"])
        print("✍️ Authors:", result["authors"])

import requests

def fetch_news(api_key, keyword):
    url = f"https://newsapi.org/v2/everything?q={keyword}&apiKey={api_key}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status() # Check for errors
        articles = response.json().get('articles', [])
        return articles
    except Exception as e:
        print(f"Error fetching news: {e}")
        return []
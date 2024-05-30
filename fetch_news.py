import requests
import json

def fetch_news():
    api_key = '04364ff9de9a46c49bea20ea5eeb62be'
    url = 'https://newsapi.org/v2/everything'
    params = {
        'apiKey': api_key,
        'q': 'foreign affairs OR economics OR politics',
        'pageSize': 10,
    }
    response = requests.get(url, params=params)
    articles = response.json().get('articles', [])
    return articles

if __name__ == "__main__":
    articles = fetch_news()
    with open('articles.json', 'w') as f:
        json.dump(articles, f)
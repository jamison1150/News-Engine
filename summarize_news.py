from transformers import pipeline
import json

summarizer = pipeline("summarization", model="EleutherAI/gpt-neo-2.7B")

def summarize_article(article):
    text = f"{article['title']} - {article['description']}"
    summary = summarizer(text, max_length=150, min_length=30, do_sample=False)
    return summary[0]['summary_text']

def summarize_news():
    with open('articles.json', 'r') as f:
        articles = json.load(f)
    summaries = [summarize_article(article) for article in articles]
    with open('summaries.json', 'w') as f:
        json.dump(summaries, f)

if __name__ == "__main__":
    summarize_news()
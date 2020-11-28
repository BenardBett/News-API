from flask import Flask
from newsapi import NewsApiClient

app = Flask(__name__)

@app.route('/')
def index():
    newsapi = NewsApiClient(api_key="d4df65110d1448f28e60b32fe558da44")
    topheadlines = newsapi.get_top_headlines(sources="abc-news")

    articles = topheadlines['articles']

    desc = []
    news = []
    url = []
    img = []


if __name__ == "__main__":
    app.run(debug=True)
    app.run
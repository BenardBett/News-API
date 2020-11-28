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
    
    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        url.append(myarticles['url'])
        img.append(myarticles['urlToImage'])
        

    mylist = zip(news, desc, url, img)

    return render_template('index.html', context=mylist)

app.route('/bbc')
def bbc():
    newsapi = NewsApiClient(api_key="d40c178ee0c6474f963ed683b651a3ab")
    topheadlines = newsapi.get_top_headlines(sources="bbc-news")

    articles = topheadlines['articles']

    desc = []
    news = []
    url = []
    img = []
    

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        url.append(myarticles['url'])
        img.append(myarticles['urlToImage'])

    mylist = zip(news, desc, url, img)

    return render_template('bbc.html', context=mylist)


if __name__ == "__main__":
    app.run(debug=True)
    app.run
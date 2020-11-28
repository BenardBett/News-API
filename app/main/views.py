from flask import Flask
from newsapi import NewsApiClient

app = Flask(__name__)




if __name__ == "__main__":
    app.run(debug=True)
    app.run
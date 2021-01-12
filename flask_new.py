from flask import Flask,render_template,redirect,url_for
from bs4 import BeautifulSoup
import requests
import json
app = Flask(__name__)

def get_data():
    json_url = requests.get("https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZxYUdjU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen")
    htmlContent = json_url.content
    soup = BeautifulSoup(htmlContent, 'html.parser')
    news_headlines = (soup.findAll("a", class_="DY5T1d",limit=10))

    news_dict = {}

    for i, news in enumerate(news_headlines, 1):
        news_dict["News" + str(i)] = news.text

    json_object = json.dumps(news_dict, indent=4)
    loaded_r = json.loads(json_object)
    return loaded_r



@app.route('/')
def Index():
    return redirect(url_for("News"))

@app.route('/today')
def News():
    loaded_r = get_data()
    return render_template('news.html',result=loaded_r)


if __name__ == "__main__":
    app.run(debug=True)
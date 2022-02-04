from flask import Flask, render_template

from newsapi import NewsApiClient


app = Flask(__name__)
API_KEY='45778e35f22c47dfadc524155cee34d6'

@app.route('/')
def index():
    newapi = NewsApiClient(API_KEY)
    topheadlines = newapi.get_top_headlines(sources="bbc-news,al-jazeera-english")

    articles = topheadlines['articles']

    news = []
    description = []
    link = []
    img = []
    time = []
    content = []
   


    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        description.append(myarticles['description'])
        link.append(myarticles['url'])
        img.append(myarticles['urlToImage'])
        time.append(myarticles['publishedAt'])
        content.append(myarticles['content'])
       


        my_list = zip( news,description,link,img,time,content)
        return render_template('index.html', context=my_list)
    
    @app.route('/alja')
    def home():
     newapi = NewsApiClient(API_KEY)
    topheadlines = newapi.get_top_headlines(sources="al-jazeera-english")

    articles = topheadlines['articles']

    news = []
    description = []
    link = []
    img = []
    time = []
    content = []
   


    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        description.append(myarticles['description'])
        link.append(myarticles['url'])
        img.append(myarticles['urlToImage'])
        time.append(myarticles['publishedAt'])
        content.append(myarticles['content'])
       


        my_list = zip( news,description,link,img,time,content )
        return render_template('headlines.html', context=my_list)
    
    
    
    if __name__ == '__main__':
     app.run(debug = True) 
        
        
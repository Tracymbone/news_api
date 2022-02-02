# from . import app

from flask import Flask, render_template
import requests
import urllib.request,json


app=Flask(__name__)
@app.route('/')
def home_page():
    base_url="https://newsapi.org/v2/everything?q=Apple&from=2022-01-25&sortBy=popularity&apiKey=45778e35f22c47dfadc524155cee34d6"
    data=requests.get(base_url).json()["articles"]
    
    return render_template('index.html',news=data)
    
@app.route('/headlines')
def headlines():
    base_url="https://newsapi.org/v2/headlines?q=Apple&from=2022-01-25&sortBy=popularity&apiKey=45778e35f22c47dfadc524155cee34d6"
    data=requests.get(base_url).json()["articles"]
      
    
    return render_template('headlines.html',news=data)
    
    

 
if __name__ == '__main__':
    app.run(debug=True)
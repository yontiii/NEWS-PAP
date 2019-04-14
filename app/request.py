from app import app
import urllib.request,json
from .models import articles,news,headlines

Articles = articles.Articles
News = news.News
Headlines = headlines.Headlines


api_key = app.congi]['NEWS_API_KEY']

# Getting the base urls

sources_url = app.config['SOURCES_URL']
articles_url = app.config['Articles_URL']
headlines_url = app.config['  HEADLINES_URL']

def get_sources(category):
     '''
    Function that gets the json response to our url request
    '''
    
    


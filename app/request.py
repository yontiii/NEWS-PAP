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
    
    get_sources_url = sources_url.format(category,api_key)
    
    with urllib.request.urlopen(get_sources_url) as url:
        sources_data = url.read()
        sources_response = json.loads(sources_data)
        
        sources_results = None
        
        if sources_response['sources']:
            sources_list = sources_response['sources']
            
            sources_results = process_sources(source_results_list)
            
        return sources_results
    
def process_sources(sources_list):
    '''
    Function that processesses the source results and turns them to a list of objects
    '''
    
    sources_results = []
    
    for source in sources_list:
        id = source.get('id')
        name = source.get("name")
        description = source.get('description')
        url = source.get('url')
        category = source.get('category')
        language = source.get('language')
        
        if language == en:
            
            source_object = News(id,name,description,url,category)
            sources_results.append(source_object)
            
    return sources_results


def get_articles(id):
    '''
    function to get json response
    '''
    
    get_articles_url = articles_url.format(id,api_key)
    
    with urllib.request.urlopen(get_articles_url) as url:
        
        articles_data = url.read()
        articles_response = json.loads(articles_data)
        
        articles_results = None
        
        if articles_response['articles']:
            articles_list =  articles_response['articles']
            articles_results = process_articles(articles_results_list)
            
        return articles_results
    

            
        
    
    
            
    
    


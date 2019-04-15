from flask import render_template
from app import app
from .request import get_sources,get_articles

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    
    
    title = 'Quick Facts | Instant News'
    news_sources = get_sources('general')
    print(news_sources)
    
    
    return render_template('index.html',title = title, sources =news_sources)

@app.route('/articles/<id>')
def articles(id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    
    articles = get_articles(id)
    return render_template('articles.html',id = id, articles=articles)
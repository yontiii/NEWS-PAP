from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    
    message = 'Hello world'
    
    return render_template('index.html',nessage = message)

@app.route('/articles/<id>')
def articles(id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('articles.html',id = id)
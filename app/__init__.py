from flask import Flask
from .config import DevConfig

# Initializing application
app = Flask(__name__,instance_relative_config = True)
from flask_bootstrap import Bootstrap

# Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

# Initializing Flask Extensions
bootstrap = Bootstrap(app)


from app import views

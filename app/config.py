class Config:
    '''
    General configuration parent class
    '''
    
    NEWS_URL = 'https://newsapi.org/v2/sources?category={}&language=en&apiKey={}'
    ARTICLES_URL = 'https://newsapi.org/v2/everything?sources={}&language=en&apiKey={}'
    HEADLINES_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
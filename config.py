import os

class Config:
    '''
    General configuration parent class
    '''
    
    TOPNEWS_API_BASE_URL ='https://newsapi.org/v2/top-headlines?sources={}&apiKey=0cfbe113f27e4c7cb88279e437d8b67d'
    CATEGORIES_API_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey=0cfbe113f27e4c7cb88279e437d8b67d'
    ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey=0cfbe113f27e4c7cb88279e437d8b67d'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


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

config_options = {
'development':DevConfig,
'production':ProdConfig
}
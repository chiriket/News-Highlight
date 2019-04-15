import os

class Config:

    SOURCES_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    EVERYTHING_SOURCE_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&pageSize={}&apiKey={}'
    EVERYTHING_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&api_key={}'
    TOP_HEADLINES_BASE_URL = 'https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
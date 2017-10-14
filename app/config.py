import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
# os.urandom(24).encode('hex')
    STATIC_URL = '/static/'
    STATIC_PATH = '/static/'


class DevelopmentConfig(Config):
    DEBUG = True
    port = 8000

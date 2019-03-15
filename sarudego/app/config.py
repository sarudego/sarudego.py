import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
# os.urandom(24).encode('hex')
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    # TOP_LEVEL_DIR = os.path.abspath(os.curdir)
    STATIC_URL = '/static/'
    STATIC_PATH = '/static/'


class DevelopmentConfig(Config):
    DEBUG = True
    port = 8000

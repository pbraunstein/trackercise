import os
from random import choice

home_dir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY_CHAR_SET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    SECRET_KEY_LENGTH = 60
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SECRET_KEY = 'this_is_secret'


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = False


class LocalConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True

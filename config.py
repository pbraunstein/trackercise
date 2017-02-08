import os

home_dir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'fake-db'
    SECRET_KEY = os.environ.get('TRACKERCISE_SECRET_KEY') or 'not-really-that-secret'


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = False


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/trackercise_test_db'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

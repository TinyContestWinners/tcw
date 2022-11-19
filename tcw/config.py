import os

class BaseConfig:
    PROJECT = 'tiny contest winners'
    DEBUG = False
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv('FLASK_SECRET', 'TerribleLifeChoices')
    WTF_CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = os.getenv('FLASK_SECRET', 'TerribleLifeChoices')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite://')
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Development(BaseConfig):
    DEBUG = True
    TESTING = True
    CSRF_ENABLED = False
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class Production(BaseConfig):
    SERVER_NAME = 'tinycontestwinners.com'

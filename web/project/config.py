import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://" + os.path.join(basedir, 'db.sqlite'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_SORT_KEYS = False
    SECRET_KEY = os.getenv("SECRET_KEY")
    ENV = 'development'
    DEBUG = True
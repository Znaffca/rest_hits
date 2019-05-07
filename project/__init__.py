import os
from flask import Flask
from project.api import api_bp
from project.models import db, ma


def create_app(config_filename=None):
    app = Flask(__name__, instance_relative_config=True)
    # basedir = os.path.abspath(os.path.dirname(__file__))
    #
    # app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
    # app.config["ALLOW_TRACK_MODIFICATIONS"] = False
    # app.config["JSON_SORT_KEYS"] = False
    # app.config["SECRET_KEY"] = 'aloha'
    # app.DEBUG = True
    app.config.from_pyfile(config_filename)
    # with app.app_context():
    db.init_app(app)
    ma.init_app(app)
    app.register_blueprint(api_bp)
    return app

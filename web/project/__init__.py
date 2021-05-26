from flask import Flask
from project.api import api_bp
from project.models import db, ma
from project.config import Config


def create_app(config_object=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_object)
    # with app.app_context():
    db.init_app(app)
    ma.init_app(app)
    app.register_blueprint(api_bp)
    return app

config_obj = Config()
app = create_app(config_obj)

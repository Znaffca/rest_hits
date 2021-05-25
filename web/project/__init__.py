from flask import Flask
from project.api import api_bp
from project.models import db, ma


def create_app(config_filename=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)
    # with app.app_context():
    db.init_app(app)
    ma.init_app(app)
    app.register_blueprint(api_bp)
    return app

app = create_app("api.cfg")
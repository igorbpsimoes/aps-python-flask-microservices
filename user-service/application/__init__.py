# application/__init__.py
import config
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    environment_configuration = os.environ['CONFIGURATION_SETUP']
    app.config.from_object(environment_configuration)

    db.init_app(app)

    with app.app_context():
        # Register blueprints
        from .orcamento_api import orcamento_api_blueprint
        app.register_blueprint(orcamento_api_blueprint)
        return app

# application/__init__.py
import config
import os
from flask import Flask
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()
UPLOAD_FOLDER = 'application/static/images'


def create_app():
    app = Flask(__name__, static_folder='static')
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    environment_configuration = os.environ['CONFIGURATION_SETUP']
    app.config.from_object(environment_configuration)

    bootstrap.init_app(app)

    with app.app_context():
        from .frontend import frontend_blueprint
        app.register_blueprint(frontend_blueprint)

        return app

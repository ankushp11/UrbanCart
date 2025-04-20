from flask import Flask
from .config import CONFIG_BY_ENV_NAME 
from .routes import register_blueprints

def create_app(env='development'):
    app = Flask(__name__)
    app.config.from_object(CONFIG_BY_ENV_NAME.get(env))

    register_blueprints(app)

    return app

from flask import Flask
import os

from route_registry import register_routes
from blueprint_registry import register_bluprints
from config import config

app = Flask(__name__)

env = os.environ.get("env").lower()

if env == "development":
    app.config.from_object(config.DevelopmentConfig)
elif env == "production":
    app.config.from_object(config.ProductionConfig)


register_routes()
register_bluprints(app)


if __name__ == "__main__":
    app.run()

from flask import Flask
import os

from Config import config
from route_registry import register_routes
from blueprint_registry import regitser_blueprints

app = Flask(__name__)


env = os.environ.get("ENV").lower()

if env == "development":
    app.config.from_object(config.DevelopmentConfig)
elif env == "production":
    app.config.from_object(config.ProductionConfig)


register_routes()
regitser_blueprints(app)


if __name__ == "__main__":
    host = os.environ.get("DEFAULT_SERVICE_HOST")
    port = os.environ.get("DEFAULT_SERVICE_PORT")
    app.run(host=host, port=port)

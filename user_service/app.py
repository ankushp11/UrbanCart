from flask import Flask
import os

from Config import config

app = Flask(__name__)


env = os.environ.get("ENV").lower()

if env == "development":
    app.config.from_object(config.DevelopmentConfig)
elif env == "production":
    app.config.from_object(config.ProductionConfig)




@app.route('/')
def home():
    return "User service is up and working."


if __name__ == "__main__":
    host = os.environ.get("DEFAULT_SERVICE_HOST")
    port = os.environ.get("DEFAULT_SERVICE_PORT")
    app.run(host=host, port=port)
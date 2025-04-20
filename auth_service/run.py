import os
from app import create_app


if __name__ == "__main__":
    env = os.environ.get("ENV").lower()
    host = os.environ.get("DEFAULT_SERVICE_HOST")
    port = os.environ.get("DEFAULT_SERVICE_PORT")
    app = create_app(env)
    app.run(host=host, port=port)

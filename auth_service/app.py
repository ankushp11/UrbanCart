from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import MetaData
from route_registry import register_routes
from blueprint_registry import register_bluprints
from config import config
from common.commands.migration_manager import DatabaseMigrationManager
from common.utils.helper import register_migration_commands

app = Flask(__name__)

env = os.environ.get("ENV").lower()

if env == "development":
    app.config.from_object(config.DevelopmentConfig)
elif env == "production":
    app.config.from_object(config.ProductionConfig)


metadata = MetaData(naming_convention=app.config["NAMING_CONVENTION"])

db = SQLAlchemy(app, metadata=metadata)

migrate = Migrate(app, db)

migration_manager = DatabaseMigrationManager(db)

register_routes()
register_bluprints(app)
register_migration_commands(app, migration_manager)

if __name__ == "__main__":
    host = os.environ.get("DEFAULT_SERVICE_HOST")
    port = os.environ.get("DEFAULT_SERVICE_PORT")
    app.run(host=host, port=port)

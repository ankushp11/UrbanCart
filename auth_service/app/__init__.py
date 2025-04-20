from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import MetaData
from .routes import register_bluprints
from .config import CONFIG_BY_ENV_NAME
from common.commands.migration_manager import DatabaseMigrationManager
from common.utils.helper import register_migration_commands


metadata = MetaData()
db = SQLAlchemy(metadata=metadata)
migrate = Migrate()
migration_manager = DatabaseMigrationManager(db)


def create_app(env='development'):
    app = Flask(__name__)
    app.config.from_object(CONFIG_BY_ENV_NAME.get(env))
    
    naming_convention = app.config.get("NAMING_CONVENTION")
    if naming_convention:
        metadata.naming_convention = naming_convention
    
    db.init_app(app)
    migrate.init_app(app, db)

    register_bluprints(app)
    register_migration_commands(app, migration_manager)

    return app

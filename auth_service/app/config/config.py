from common.constants.db_config import DatabaseConnectionConfig


class Config:
    DEBUG = False
    SERVICE_NAME = "auth"
    SERVICE_DB_NAME = "auth_db"

    NAMING_CONVENTION = DatabaseConnectionConfig.NAMING_CONVENTION
    SQLALCHEMY_TRACK_MODIFICATIONS = (
        DatabaseConnectionConfig.SQLALCHEMY_TRACK_MODIFICATIONS
    )
    SQLALCHEMY_ECHO = DatabaseConnectionConfig.SQLALCHEMY_ECHO
    SQLALCHEMY_ENGINE_OPTIONS = DatabaseConnectionConfig.SQLALCHEMY_ENGINE_OPTIONS
    SQLALCHEMY_DATABASE_URI = DatabaseConnectionConfig.get_database_uri(
        SERVICE_NAME, SERVICE_DB_NAME
    )


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    pass

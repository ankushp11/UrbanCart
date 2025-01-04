import os


class DatabaseConnectionConfig:
    NAMING_CONVENTION = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SQLALCHEMY_ECHO = False

    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_recycle": 3600,  # Recycle connections after 1 hour
        "pool_size": 20,  # Max 10 connections in the pool
        "max_overflow": 10,  # Allow 5 additional connections over the pool size
        "pool_timeout": 300,  # Wait for 300 seconds (5 min) for db to get connected before timing out.
    }

    @staticmethod
    def get_database_uri(service_name, service_db_name):
        """Returns the database URI for the given service name."""
        if not service_db_name:
            raise ValueError(f"Database name not found for service: {service_name}.")

        db_username = os.environ.get("DB_USERNAME")
        db_password = os.environ.get("DB_PASSWORD")
        db_host = os.environ.get("DB_HOST")
        db_port = os.environ.get("DB_PORT")
        db_name = service_db_name

        if not db_username or not db_password or not db_host or not db_port:
            raise ValueError(
                "Database credentials or host/port not found in environment variables."
            )

        service_db_uri = (
            f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"
        )

        return service_db_uri

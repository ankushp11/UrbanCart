import os


class Config:
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = f"postgresql://{os.environ.get('DB_USERNAME')}:{os.environ.get('DB_PASSWORD')}@{os.environ.get('DB_HOST')}:{os.environ.get('DB_PORT')}/{os.environ.get('DB_NAME')}"


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    pass

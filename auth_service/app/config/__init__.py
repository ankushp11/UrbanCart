from .config import DevelopmentConfig, ProductionConfig


CONFIG_BY_ENV_NAME = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}

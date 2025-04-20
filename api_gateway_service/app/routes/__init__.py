from .services_handler import service_handler


def register_blueprints(app):
    app.register_blueprint(service_handler, url_prefix="/")

from routes.services_handler import service_handler


def regitser_blueprints(app):
    app.register_blueprint(service_handler, url_prefix="/")

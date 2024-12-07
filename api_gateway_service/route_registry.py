from routes.services_handler import service_handler, ServiceRouter

def register_routes():
    service_handler.add_url_rule('/<string:service_name>/<path:path>', view_func=ServiceRouter.as_view("service_router"))

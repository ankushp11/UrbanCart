from flask import Blueprint, request
from flask.views import MethodView
import httpx

from constants.services import Services
from constants.messages import ErrorMessages, HTTPStatusCodes
from utils.helper import make_response


service_handler = Blueprint(name="service_handler", import_name="__name__")


class ServiceRouter(MethodView):
    """Handles each incoming request and routes it the respective service."""

    methods = ["GET", "POST", "PUT", "DELETE", "PATCH"]

    def dispatch_request(self, service_name, path, *args, **kwargs):
        if service_name not in Services.SERVICES_LIST:
            return make_response(
                message=ErrorMessages.PAGE_NOT_FOUND_ERR,
                status_code=HTTPStatusCodes.NOT_FOUND,
            )

        SERVICE_ROUTES = Services.SERVICE_ROUTES
        requested_service_url = SERVICE_ROUTES.get(service_name)
        if not requested_service_url:
            return make_response(
                message=ErrorMessages.SERVICE_ENDPOINT_UNAVAILABLE_ERR,
                status_code=HTTPStatusCodes.NOT_FOUND,
            )

        target_url = f"{requested_service_url}/{service_name}/{path}"
        request_method = request.method
        request_headers = request.headers
        json_data = request.get_json(silent=True)
        params = request.args
        with httpx.Client() as client:
            response = client.request(
                method=request_method,
                url=target_url,
                headers=request_headers,
                data=json_data,
                params=params,
            )
            return response.json()

from flask import Blueprint, jsonify
from flask.views import MethodView


login_bp = Blueprint(name="login", import_name="__name__")


class LoginUserAPI(MethodView):
    methods = ["GET"]

    def get(self):
        return jsonify({"message": "Login user API working!!"}), 200


class RegisterUserAPI(MethodView):
    methods = ["GET"]

    def get(self):
        return jsonify({"message": "Register user API working!!"}), 200


#  register urls/endpoints to the blueprint
def register_routes():
    # login endpoint
    login_bp.add_url_rule(
        "/login/", view_func=LoginUserAPI.as_view("login_api")
    )

    # register endpoint
    login_bp.add_url_rule(
        "/register/", view_func=RegisterUserAPI.as_view("register_api")
    )

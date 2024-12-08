from flask import Blueprint, jsonify, make_response
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

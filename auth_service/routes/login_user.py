from flask import Blueprint, jsonify, make_response
from flask.views import MethodView


login_bp = Blueprint(name="login", import_name="__name__")


class LoginUserAPI(MethodView):
    methods = ["GET"]

    def get(self):
        return make_response(jsonify({"message": "Login user API working!!", "status_code": 200}))


class RegisterUserAPI(MethodView):
    methods = ["GET"]
    
    def get(self):
        return make_response(jsonify({"message": "Register user API working!!", "status_code": 200}))

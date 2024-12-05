from flask import Blueprint
from flask.views import MethodView


login_bp = Blueprint(name="login", import_name="__name__")


class LoginUserAPI(MethodView):
    methods = ["GET"]

    def get(self):
        return "Login user API."


class RegisterUserAPI(MethodView):
    methods = ["GET"]
    
    def get(self):
        return "Register User API."

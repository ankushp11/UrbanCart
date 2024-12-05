from routes.login_user import login_bp
from routes import login_user


def register_routes():
    # login endpoint
    login_bp.add_url_rule(
        "/login/", view_func=login_user.LoginUserAPI.as_view("login_api")
    )

    # register endpoint
    login_bp.add_url_rule(
        "/register/", view_func=login_user.RegisterUserAPI.as_view("register_api")
    )

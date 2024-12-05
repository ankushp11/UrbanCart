from routes.login_user import login_bp


def register_bluprints(app):
    app.register_blueprint(login_bp, url_prefix="/auth/")

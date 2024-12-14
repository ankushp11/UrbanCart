class Services:
    SERVICES_LIST = ["auth", "user"]

    SERVICE_ROUTES = {
        "auth": "http://auth_service:5000",
        "user": "http://user_service:5000",
    }

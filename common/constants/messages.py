class Messages:
    pass


class ErrorMessages(Messages):
    PAGE_NOT_FOUND_ERR = "Unable to find the page you are looking for."
    INTERNAL_SERVER_ERR = "Server is not able to "
    METHOD_NOT_ALLOWED_ERR = "The HTTP method is not allowed for this endpoint."
    DATABASE_CONNECTION_ERR = ""
    SERVICE_UNAVAILABLE_ERR = (
        "The service is temporarily unavailable. Please try again later."
    )
    SERVICE_ENDPOINT_UNAVAILABLE_ERR = "Endpoint not available for the request service."
    SERVICE_DB_NAME_NOT_FOUND = "Database name not found for the service"


class HTTPStatusCodes:
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    NO_CONTENT = 204
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    METHOD_NOT_ALLOWED = 405
    CONFLICT = 409
    UNPROCESSABLE_ENTITY = 422
    TOO_MANY_REQUESTS = 429
    INTERNAL_SERVER_ERROR = 500
    BAD_GATEWAY = 502
    SERVICE_UNAVAILABLE = 503
    GATEWAY_TIMEOUT = 504

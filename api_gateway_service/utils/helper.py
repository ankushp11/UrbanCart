from flask import jsonify, Response


def make_response(message, status_code, data=None, errors=None, pagination=None):
    """
    General utility function to create consistent API responses.

    :param message: A string describing the result of the request.
    :param status_code: HTTP status code for the response.
    :param data: Optional data to include in the response.
    :param errors: Optional error details (e.g., validation errors).
    :param pagination: Optional pagination metadata (e.g., total_count, page, per_page).
    :return: Flask JSON response object with a standardized structure.
    """
    response = {
        "message": message,
        "data": data,
        "errors": errors,
        "pagination": pagination,
    }

    response = {key: value for key, value in response.items() if value is not None}
    response = jsonify(response)
    response.status_code = status_code
    return response


def convert_response_from_httpx_to_flask(httpx_response):
    flask_response = Response(
        httpx_response.content,
        status=httpx_response.status_code,
        headers=dict(httpx_response.headers),
    )
    return flask_response

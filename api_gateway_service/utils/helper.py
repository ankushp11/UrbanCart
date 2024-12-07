from flask import jsonify


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
    return jsonify(response), status_code

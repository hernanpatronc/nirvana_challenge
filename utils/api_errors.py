from flask import current_app


class APIError(Exception):
    """All custom API Exceptions"""
    pass


class APIBadRequestError(APIError):
    """Custom Bad Request Error Class."""
    code = 400
    description = "Bad Request Error"


class APIConnectException(APIError):
    """Error connecting with APIs."""
    code = 500
    url = ''
    message = 'Error'
    description = 'Error connecting to API'

from flask import Blueprint, jsonify
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import NotFound

errors_bp = Blueprint('errors', __name__)


@errors_bp.app_errorhandler(404)
def not_found_error(error):
    response = jsonify({'message': 'Not Found', 'error': error.description})
    response.status_code = 404
    return response


@errors_bp.app_errorhandler(500)
def internal_error(error):
    response = jsonify({'message': 'Internal Server Error', 'error': error.description})
    response.status_code = 500
    return response


@errors_bp.app_errorhandler(Exception)
def handle_all_exceptions(error):
    response = jsonify({'message': 'An unexpected error occurred', 'error': str(error)})
    response.status_code = 500
    return response

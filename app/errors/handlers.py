from http import HTTPStatus
from flask import render_template
from app import db
from app.errors import bp


@bp.app_errorhandler(HTTPStatus.NOT_FOUND)
def not_found_error(error):
    return render_template('errors/404.html'), HTTPStatus.NOT_FOUND


@bp.app_errorhandler(HTTPStatus.INTERNAL_SERVER_ERROR)
def internal_error(error):
    db.session.rollback()
    return render_template('errors/500.html'), HTTPStatus.INTERNAL_SERVER_ERROR

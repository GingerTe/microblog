from http import HTTPStatus
from flask import render_template
from app import app, db


@app.errorhandler(HTTPStatus.NOT_FOUND)
def not_found_error(error):
    return render_template('404.html'), HTTPStatus.NOT_FOUND


@app.errorhandler(HTTPStatus.INTERNAL_SERVER_ERROR)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), HTTPStatus.INTERNAL_SERVER_ERROR

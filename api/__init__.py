#!/usr/bin/python3
"""Initialize the flask app"""

from flask import Flask
from os import getenv
from api.views import app_views


def create_app():
    """creates Flask and registers blueprint instance"""
    app = Flask(__name__)
    app.secret_key = getenv('MY_SECRET_KEY')

    # Registers blueprint
    app.register_blueprint(app_views)

    return app

#!/usr/bin/python3
""" A flask application """

from flask import Flask, jsonify, make_response
from models import storage
from api.v1.views import app_views
from os import environ


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_storage(error):
    """ close storage on error and after every request"""
    storage.close()


@app.errorhandler(404)
def error404(error):
    """ Handles 404 error """
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    """ Run only when executed as main function """
    host = environ.get('HBNB_API_HOST')
    port = environ.get('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
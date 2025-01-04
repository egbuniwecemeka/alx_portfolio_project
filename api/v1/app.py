#!/usr/bin/python3
"""A python script with endpoints(routes) to API"""

from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def reload():
    """"""
    storage.close()


@app.errorhandler(404)
def error():
    """Returns 404 status code on error"""
    return jsonify({'error': 'Not found'})


if __name__ == '__main__':
    host_user = getenv('HBNB_API_HOST') | '0.0.0.0'
    port_user = getenv('HBNB_API_PORT') | 5000
    app.run(host=host_user, port=port_user)
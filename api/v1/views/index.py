#!/usr/bin/python3
""""""

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'])
def status():
    """Returns the status of the API"""
    return jsonify({'status': 'OK'})


@app_views.route('/stats', methods=['GET'])
def stats():
    """Retrieves the number of objects by type"""
    return storage.count()
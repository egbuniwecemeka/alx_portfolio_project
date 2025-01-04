#!/usr/bin/python3
"""Index, routes and methods"""

from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Returns the status of the API"""
    return jsonify({'status': 'OK'})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """Retrieves the number of each objects by type"""
    classes = [Amenity, City, Place, Review, State, User]
    names = ['amenities', 'cities', 'places', 'states', 'users']
    num_objs = {}
    for obj in range(len(classes)):
        num_objs[names[obj]] = storage.count(classes[obj])
    return jsonify(num_objs)

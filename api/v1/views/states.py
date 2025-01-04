#!/usr/bin/python3
"""Module that handles all State objects default RESTFul API actions"""

from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.state import State

@app_views.route('/states', methods=['GET'])
def all_states():
    """Retrieves all states objects"""
    states = storage.all(State)
    return [state for state in states]


@app_views.route('/states/<int:state_id>', methods=['GET'])
def state(state_id):
    """Retrieves a state object using its id, else raise a 404 error"""
    states = storage.all(State)
    id = f'{states}.{state_id}'
    for key, value in states.items():
        if id not in states[key]:
            raise TypeError(404)
        else:
            return jsonify({states[key]: states[value]})


@app_views.route('/states/<int:state_id>', methods=['DELETE'])
def del_state(state_id):
    pass

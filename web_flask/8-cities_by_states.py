#!/usr/bin/python3
""" A python script that renders content using Flask"""

from flask import Flask, render_template
from models import storage
from models.state import State
from os import getenv


app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception=None):
    """Closes the current session"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def state_cities():
    """"""
    states = storage.all(State)
    #Use city relationship if storage is DBStorage
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        state_list = [(state.id, state.name, state.cities) for state in states.values()]
    else:
        state_list = [(state.id, state.name, state.cities) for state in states.values()]
    
    return render_template('8-cities_by_states.html', states=state_list)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

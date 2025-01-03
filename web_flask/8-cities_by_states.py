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
    """Render cities assocoated to a state"""
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

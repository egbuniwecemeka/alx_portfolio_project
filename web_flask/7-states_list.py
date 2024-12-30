#!/usr/bin/python3

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """"""
    data = storage.all(State)
    return render_template('7-states_list.html', data=data)


@app.teardown_appcontext
def remove_session(exception=None):
    """Removes the current session"""
    storage.close()
#!/usr/bin/python3
"""A python script with endpoints(routes) to API"""

from flask import Flask
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def reload():
    """"""
    storage.close()

#!/usr/bin/python3
"""A module for my cart routes"""

from flask import Flask


app = Flask(__name__)


@app.route('/cart', method=['GET'], strict_slashes=False)
def cart():
    pass
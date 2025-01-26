#!/usr/bin/python3
"""A script that renders the result page"""

from api.views import app_views
from flask import render_template

@app_views.route('/results', methods=['GET'], strict_slashes=False)
def results():
    """Renders the results HTML template"""
    return render_template('results.html')
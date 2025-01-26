#!/usr/bin/python3
"""A script that creates a contact route"""

from api.views import app_views
from flask import render_template


@app_views.route('/contact', methods=['GET'], strict_slashes=False)
def contact_page():
    """Contact page"""
    return render_template('contact.html')
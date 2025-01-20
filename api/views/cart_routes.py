#!/usr/bin/python3
"""A module for my cart routes"""

from api.views import app_views
from flask import render_template

# Route to cart
@app_views.route('/cart', methods=['GET', 'POST'], strict_slashes=False)
def cart():
    return render_template('cart.html')
#!/usr/bin/python3
"""Initializes of Flask app and Blueprints"""

from flask import  Blueprint

# Creste a Blueprint instance
app_views = Blueprint('app_views', __name__, url_prefix='/')

# Import routes into the Blueprint for registration
from api.views.home_route import *
from api.views.cart_routes import *
from api.views.quiz_routes import *
from api.views.contact_route import *

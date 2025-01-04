#!/usr/bin/python3
"""Module that creates a Blueprint instance for API routes"""

from flask import Blueprint


# Create a Blueprint instance
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import routes into the Blueprint
from api.v1.views.index import * # PEP8 may complain
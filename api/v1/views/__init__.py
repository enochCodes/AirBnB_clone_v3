#!/usr/bin/python3
"""
Initialize the views for the Flask web application.
"""

from flask import Blueprint
from index import *


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

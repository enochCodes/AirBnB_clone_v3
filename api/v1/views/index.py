#!/usr/bin/python3
"""
Index module for the Flask web application.
"""
from flask import jsonify
from views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """
    Get the status of the API.
    """
    return jsonify({"status": "OK"})

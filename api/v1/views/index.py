#!/usr/bin/python3xx
'''api status'''
import models
from models import storage
from models.base_model import BaseModel
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False)
def returnstuff():
    '''return stuff'''
    return jsonify(status='OK')


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def get_stats():
    """
    Retrieves the number of each object by type
    """
    stats = {
            'amenities': Amenity, 'users': User,
            'states': State, 'cities': City,
            'places': Place, 'reviews': Review}
    for key in stats:
        stats[key] = storage.count(stats[key])
    return jsonify(stats)

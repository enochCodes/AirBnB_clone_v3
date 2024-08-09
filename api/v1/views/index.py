#!/usr/bin/python3
'''api status'''
import models
from models import storage
from models.base_model import BaseModel
from flask import jsonify
from api.v1.views import app_views
from models.amenity import Amenity
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review

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

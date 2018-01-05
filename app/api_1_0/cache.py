
from flask import jsonify
from flask.globals import request
from werkzeug.utils import secure_filename

import predix.data.cache

from . import api

pc = predix.data.cache.Cache()

@api.route('/keys')
def keys():
    keys = []
    for key in pc.connection.scan_iter():
        keys.append(key)

    return jsonify(keys)

@api.route('/cache/<key>', methods=['POST'])
def set_cache(key):
    value = request.body
    pc.set(key, request.values)

@api.route('/cache/<key>', methods=['GET'])
def get_cache(key):
    pc2 = predix.data.cache.Cache()
    return jsonify(pc2.get(key))

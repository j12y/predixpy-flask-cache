
from flask import render_template
from flask import request

from . import ui

import predix.data.cache

pc = predix.data.cache.Cache()

@ui.route('/')
def index():
    """
    Trivial little demo of a form with some bad UX.
    """
    key = request.args.get('key') or ''
    value = request.args.get('value') or ''
    msg = ''

    if key and value:
        pc.set(key, value)
        msg = 'Success'
    elif key:
        value = pc.get(key)
        if not value:
            msg = 'No value cached for key "{}".'.format(key)
    elif value:
        msg = 'Must define a key to store that new value.'

    # Consider demonstrating delete value from key

    return render_template('index.html', key=key, value=value, msg=msg)

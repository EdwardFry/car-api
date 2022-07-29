from flask import Blueprint, request, jsonify
from cache import *

route_post_colours = Blueprint('route_post_colours', __name__)

@route_post_colours.route('/', methods=['POST'])
def post_colours():
    try:
        colours = request.get_json()['colours']
        for c in colours:
            name = c['name']
            colour_storage.append(name)
        return "success", 200
    except:
        return 'incorrect json format', 400
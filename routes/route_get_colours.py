from flask import Blueprint, request, jsonify
from cache import *

route_get_colours = Blueprint('route_get_colours', __name__)

@route_get_colours.route('/', methods=['GET'])
def get_colours():
    data = []
    colours_dict = colour_storage.get_data()
    for key in colours_dict:
        colour = colours_dict[key]
        data.append(
            {
                'id': key,
                'name': colour
            }
        )

    result = {
        'status': 'ok',
        'data': data
    }

    return jsonify(result), 200
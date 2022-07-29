from flask import Blueprint, request, jsonify
from cache import *

route_get_colour_by_id = Blueprint('route_get_colour_by_id', __name__)

# GET /COLOUR/<ID>
@route_get_colour_by_id.route('<id>', methods=['GET'])
def get_colour_by_id(id):
    if not id.isdigit():
        return "id must be an integer", 400
    id = int(id)

    if not colour_storage.is_element_stored(id):
        return ''.join(['Colour with id: ', str(id) , ' not found']), 404

    colour = colour_storage.get_data()[id]
    data = {
        'id': id,
        'name': colour
    }
    result = {
        'status': 'ok',
        'data': data
    }

    return result, 200

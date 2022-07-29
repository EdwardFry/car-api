from flask import Blueprint, request, jsonify
from cache import *

route_delete_colour = Blueprint('route_delete_colour', __name__)

# DELETE /COLOUR/<ID>
@route_delete_colour.route('<id>', methods=['DELETE'])
def delete_colour(id):
    if not id.isdigit():
        return "id must be an integer", 400

    id = int(id)
    if not colour_storage.is_element_stored(id):
        return ''.join(['Colour with id: ', str(id) , ' not found']), 404

    colour_storage.delete(id)
    return "successfully deleted", 200

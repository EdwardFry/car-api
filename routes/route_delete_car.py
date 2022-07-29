from flask import Blueprint, request, jsonify
from cache import *

route_delete_car = Blueprint('route_delete_car', __name__)

@route_delete_car.route('<id>', methods=['DELETE'])
def delete_car(id):
    if not id.isdigit():
        return "id must be an integer", 400
    id = int(id)
    if not car_storage.is_element_stored(id):
        return ''.join(['Car with id: ', str(id) , ' not found']), 404

    car_storage.delete(id)
    return "successfully deleted", 200
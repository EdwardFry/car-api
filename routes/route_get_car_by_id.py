from flask import Blueprint, request, jsonify
from cache import *

route_get_car_by_id = Blueprint('route_get_car_by_id', __name__)

# GET /CAR/<ID>
@route_get_car_by_id.route('<id>', methods=['GET'])
def get_car_by_id(id):
    if not id.isdigit():
        return "id must be an integer", 400
    id = int(id)

    if not car_storage.is_element_stored(id):
        print("not stored")
        return ''.join(['Car with id: ', str(id) , ' not found']), 404

    car = car_storage.get_data()[id]
    data = {
        'id': id,
        'make': car.make,
        'model': car.model,
        'build_date': car.build_date,
        'colour_id': car.colour_id
    }
    result = {
        'status': 'ok',
        'data': data
    }

    return result, 200

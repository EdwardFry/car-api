from flask import Blueprint, request, jsonify
from cache import *

route_get_cars = Blueprint('route_get_cars', __name__)

@route_get_cars.route('/',  methods=['GET'])
def get_cars():
    data = []
    cars_dict = car_storage.get_data()
    for key in cars_dict:
        car = cars_dict[key]
        data.append(
            {
                'id': key,
                'make': car.make,
                'model': car.model,
                'build_date': car.build_date,
                'colour_id': car.colour_id
            }
        )
    result = {
        'status': 'ok',
        'data': data
    }
    return jsonify(result), 200

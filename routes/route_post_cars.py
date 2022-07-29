from flask import Blueprint, request, jsonify
from cache import *

route_post_cars = Blueprint('route_post_cars', __name__)

@route_post_cars.route('/',  methods=['POST'])
def cars():
    try: 
        json = request.get_json()['cars']

        for car in json:
            make = car['make']
            model = car['model']
            build_date = car['build_date']
            colour_id = int(car['colour_id'])
            car = Car(make, model, build_date, colour_id)
            car_storage.append(car)
    except:
        return 'incorrect json format', 400

    if not colour_storage.is_element_stored(colour_id):
        return ''.join(['colour with colour id: ', colour_id, ' not found']), 404

    return 'data saved', 200

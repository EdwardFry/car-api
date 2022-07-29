from flask import Flask, request, jsonify, Blueprint
from cache import *

from routes.home import route_home

from routes.route_get_cars import route_get_cars
from routes.route_post_cars import route_post_cars

from routes.route_delete_car import route_delete_car
from routes.route_get_car_by_id import route_get_car_by_id

from routes.route_get_colours import route_get_colours
from routes.route_post_colours import route_post_colours

from routes.route_get_colour_by_id import route_get_colour_by_id
from routes.route_delete_colour import route_delete_colour

app = Flask(__name__)

#  GET  DOCS/HOME PAGE
app.register_blueprint(route_home, url_prefix='/')

#  GET POST  /CARS
app.register_blueprint(route_get_cars, url_prefix='/cars')
app.register_blueprint(route_post_cars, url_prefix='/cars')

#  GET DELETE  /CAR
app.register_blueprint(route_get_car_by_id, url_prefix='/car')
app.register_blueprint(route_delete_car, url_prefix='/car')

#  GET POST  /COLOURS
app.register_blueprint(route_get_colours, url_prefix='/colours')
app.register_blueprint(route_post_colours, url_prefix='/colours')

#  GET DELETE  /COLOUR
app.register_blueprint(route_get_colour_by_id, url_prefix='/colour')
app.register_blueprint(route_delete_colour, url_prefix='/colour')


if __name__ == '__main__':
    app.run(debug=True)

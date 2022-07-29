from flask import Blueprint, render_template
from cache import *

route_home= Blueprint('home', __name__)

@route_home.route('/', methods=['GET'])
def get_docs():
    return render_template('docs.html')
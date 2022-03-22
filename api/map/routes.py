from flask import Blueprint
from api.map.utils import add_all_ow_maps

map = Blueprint('map', __name__, url_prefix='/map')


@map.post('')
def add_all_maps():
    add_all_ow_maps()
    return 'MAPS ADDED'

from flask import Blueprint, jsonify
from flask_login import current_user, login_required
from utils.routes.api.map.utils import get_heroes_winrate

map = Blueprint('map', __name__, url_prefix='/map')

@map.get('/<int:map_id>/<int:hero_role_id>')
@login_required
def get_hero_stats(map_id, hero_role_id):
    hero_stats = get_heroes_winrate(user=current_user, map_id=map_id, hero_role_id=hero_role_id)
    return jsonify(hero_stats)
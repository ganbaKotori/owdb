from flask import Blueprint
from api.match.routes import match
from api.user.routes import user
from api.map.routes import map
from api.hero.routes import hero
from api.auth.routes  import auth

api = Blueprint('api', __name__, url_prefix='/api')

api.register_blueprint(match)
api.register_blueprint(map)
api.register_blueprint(hero)
api.register_blueprint(user)
api.register_blueprint(auth)
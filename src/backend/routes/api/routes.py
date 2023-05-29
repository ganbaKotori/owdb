from flask import Blueprint
from routes.api.match.routes import match
from routes.api.user.routes import user
from routes.api.map.routes import map
from routes.api.hero.routes import hero
from routes.api.auth.routes  import auth

api = Blueprint('api', __name__, url_prefix='/api')

api.register_blueprint(hero)
api.register_blueprint(match)
api.register_blueprint(map)
api.register_blueprint(user)
api.register_blueprint(auth)
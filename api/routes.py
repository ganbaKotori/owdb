from flask import Blueprint
from api.match.routes import match
from api.user.routes import user

api = Blueprint('api', __name__, url_prefix='/api')

api.register_blueprint(match)
api.register_blueprint(user)
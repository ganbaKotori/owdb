from flask import Blueprint
from client.auth.routes import auth
from client.dashboard.routes import dashboard
from client.match.routes import match

client = Blueprint('client', __name__)

client.register_blueprint(auth)
client.register_blueprint(dashboard)
client.register_blueprint(match)
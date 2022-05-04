from flask import Blueprint
from client.auth.routes import auth
from client.dashboard.routes import dashboard
from client.match.routes import match
from client.user.routes import user
from client.friend.routes import friend

client = Blueprint('client', __name__)

client.register_blueprint(auth)
client.register_blueprint(dashboard)
client.register_blueprint(match)
client.register_blueprint(user)
client.register_blueprint(friend)
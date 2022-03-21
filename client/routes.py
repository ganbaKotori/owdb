from flask import Blueprint
from client.auth.routes import auth
from client.dashboard.routes import dashboard

client = Blueprint('client', __name__)

client.register_blueprint(auth)
client.register_blueprint(dashboard)
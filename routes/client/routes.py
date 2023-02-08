from flask import Blueprint
from routes.client.auth.routes import auth
from routes.client.dashboard.routes import dashboard
from routes.client.match.routes import match
from routes.client.user.routes import user
from routes.client.friend.routes import friend
from routes.client.map.routes import ow_map
from flask import render_template, redirect, url_for
from flask_login import current_user

client = Blueprint('client', __name__)

client.register_blueprint(auth)
client.register_blueprint(dashboard)
client.register_blueprint(match)
client.register_blueprint(user)
client.register_blueprint(friend)
client.register_blueprint(ow_map)

@client.get('/')
def get_landing_page():
    if current_user.is_authenticated:
        return redirect(url_for('client.dashboard.user_dashboard'))
    return render_template('index.html')
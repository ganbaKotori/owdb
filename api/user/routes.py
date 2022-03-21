from flask import make_response, jsonify, redirect, url_for, Blueprint
from flask_login import login_user
from api.user.models import User 

user = Blueprint('user', __name__, url_prefix='/user')

@user.route('/users')
def get_users():
    users = User.query.all()
    return make_response(jsonify(users),200)
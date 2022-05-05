from flask import make_response, jsonify, redirect, url_for, Blueprint, request
from flask_login import current_user
from api.user.models import User 
from app import db


user = Blueprint('user', __name__, url_prefix='/user')

@user.get('')
def get_users():
    keyword = request.args.get('keyword')
    users = User.query.filter(User.username.ilike(f'%{keyword}%')).all()
    return make_response(jsonify(users),200)

@user.post('/<string:user_username>/send_friend_request')
def send_friend_request(user_username):
    requested_user = User.query.filter(User.username==user_username).first()
    print(requested_user)
    current_user.send_friend_request(requested_user.id)
    db.session.commit()
    return make_response(jsonify(requested_user),200)

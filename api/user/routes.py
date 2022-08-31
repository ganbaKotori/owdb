from flask import make_response, jsonify, redirect, url_for, Blueprint, request
from flask_login import current_user
from api.user.models import User
from app import db
import api.user.utils as utils


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
    return make_response({"response" : "Friend Request Sent!"},200)

@user.post('/friendship/<int:friendship_id>/accept')
def accept_friend_request(friendship_id):
    current_user.accept_friend_request(friendship_id)
    db.session.commit()
    return make_response("accepted",200)

@user.delete('/friendship/<int:friendship_id>')
def remove_friend(friendship_id):
    current_user.remove_friend(friendship_id)
    db.session.commit()
    return make_response("deleted",200)

@user.get('/friendship/requests')
def get_friend_requests():
    pending_requests = current_user.get_friend_requests()
    return make_response(jsonify(pending_requests),200)

@user.get('/friendship')
def get_current_user_friends():
    current_user_friends = utils.get_current_user_friends()
    return make_response(jsonify(current_user_friends),200)
    
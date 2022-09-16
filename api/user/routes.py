from flask import make_response, jsonify, redirect, url_for, Blueprint, request, flash
from flask_login import current_user
from api.user.models import User
from app import db
import api.user.utils as utils
from api.user.schema import UserSchema


user = Blueprint('user', __name__, url_prefix='/user')

@user.get('')
def get_users():
    keyword = request.args.get('keyword')
    if len(keyword) < 5:
        return make_response({'MESSAGE': 'MUST BE GREATER THAN 5 CHARACTERS'},400)
    users = User.query.filter(User.username.ilike(f'%{keyword}%')).all()
    pr_dict_list = []
    for p in users:
        friendship_schema = UserSchema()
        friendship_dict = friendship_schema.dump(p)
        pr_dict_list.append(friendship_dict)
    #return pr_dict_list
    return make_response(jsonify(pr_dict_list),200)

@user.post('/<string:user_username>/send_friend_request')
def send_friend_request(user_username):
    requested_user = User.query.filter(User.username==user_username).first()
    if requested_user.id == current_user.id:
        return make_response({"response" : "Cannot send a friend request to yourself!"},400)
    current_user.send_friend_request(requested_user.id)
    db.session.commit()
    return make_response({"response" : "Friend Request Sent!"},200)

@user.post('/friendship/<int:friendship_id>/accept')
def accept_friend_request(friendship_id):
    current_user.accept_friend_request(friendship_id)
    db.session.commit()
    flash('Friend Request successfully accepted!', 'success')
    return redirect(request.referrer)

@user.post('/friendship/<int:friendship_id>/decline')
def decline_friend_request(friendship_id):
    current_user.decline_friend_request(friendship_id)
    db.session.commit()
    return redirect(request.referrer)

@user.post('/friendship/<string:friend_username>/remove_friend')
def remove_friend(friend_username):
    current_user.remove_friend_by_username(friend_username)
    db.session.commit()
    return redirect(request.referrer)

@user.get('/friendship/requests')
def get_friend_requests():
    pending_requests = current_user.get_friend_requests()
    print(pending_requests)
    return make_response(jsonify(pending_requests),200)

@user.get('/friendship')
def get_current_user_friends():
    current_user_friends = utils.get_current_user_friends()
    return make_response(jsonify(current_user_friends),200)
    
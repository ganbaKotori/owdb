from flask import make_response, jsonify, redirect, url_for, Blueprint, request
from flask_login import current_user
from api.user.models import User 
from app import db

def get_current_user_friends():
    current_to_friend_ids = [friendship.friend_id for friendship in current_user.requested_friends if friendship.request_accepted is False]
    current_from_friend_ids = [friendship.friend_id for friendship in current_user.receieved_friends if friendship.request_accepted is False]
    friends = db.session.query(User.username).filter(User.id.in_(current_to_friend_ids + current_from_friend_ids)).all()
    return [i[0] for i in friends]

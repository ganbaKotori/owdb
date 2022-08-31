from flask import make_response, jsonify, redirect, url_for, Blueprint, request
from flask_login import current_user
from api.user.models import User, Friendship
from app import db
from sqlalchemy import or_, and_

def get_current_user_friends():
    current_to_friend_ids = [friendship.friend_id for friendship in current_user.requested_friends if friendship.request_accepted is True]
    current_from_friend_ids = [friendship.user_id for friendship in current_user.receieved_friends if friendship.request_accepted is True]
    friends = db.session.query(User.username).filter(User.id.in_(current_to_friend_ids + current_from_friend_ids)).all()
    return [i[0] for i in friends]

def get_current_user_pending_friend_requests():
    current_to_friend_ids = [friendship.friend_id for friendship in current_user.requested_friends if friendship.request_accepted is False]
    friends = db.session.query(User.username).filter(User.id.in_(current_to_friend_ids)).all()
    return [i[0] for i in friends]

def get_current_user_sent_friend_requests():
    current_to_friend_ids = [friendship.friend_id for friendship in current_user.requested_friends if friendship.request_accepted is False]
    friends = db.session.query(User.username).filter(User.id.in_(current_to_friend_ids)).all()
    return [i[0] for i in friends]

def get_current_user_relationship_status(user_id):
    relationship = {
        "following": False,
        "followed_by": False,
        "following_received": False,
        "following_requested": False,
    }

    following_status = Friendship.query.filter(and_(Friendship.user_id==current_user.id, Friendship.friend_id==user_id)).first()
    followed_by_status = Friendship.query.filter(and_(Friendship.user_id==user_id, Friendship.friend_id==current_user.id)).first()

    relationship["following"] = True if following_status else False
    relationship["following_received"] = following_status.request_accepted if following_status else False
    relationship["followed_by"] = True if followed_by_status else False
    relationship["following_requested"] = followed_by_status.request_accepted if followed_by_status else False

    return relationship

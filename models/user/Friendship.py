from flask_login import UserMixin

from dataclasses import dataclass
from app import db, login_manager    
from typing import List
from sqlalchemy import and_, func, or_
from marshmallow import Schema, fields
from flask import redirect
from models.match.Match import Match
from models.match.MatchUser import MatchUser

# @dataclass
# class Friendship(db.Model):
#     __tablename__ = "friendship"
    
#     friend_a_id = db.Column(db.Integer, primary_key=True)
#     friend_b_id = db.Column(db.Integer, primary_key=True)

#     __table_args__ = (db.ForeignKeyConstraint(
#                             ['friend_a_id', 'friend_b_id'], 
#                             ['user.id', 'user.id']), 
#                   )


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect('/login')
class Friendship(db.Model):
    __tablename__ = 'friendship'
    user_id = db.Column(db.ForeignKey('user.id') , autoincrement=False,primary_key=True)
    friend_id = db.Column(db.ForeignKey('user.id'), autoincrement=False, primary_key=True)
    id = db.Column(db.Integer, autoincrement=True, primary_key=False, unique=True, nullable=False)

    request_accepted = db.Column(db.Boolean, nullable=False, default=False)

    user = db.relationship('User',primaryjoin="User.id == Friendship.user_id")



    #active = db.Column(db.Boolean(), nullable=False, server_default='0')

    # friends = db.relationship("User", secondary=Friendship, 
    #                        primaryjoin=id==Friendship.friend_a_id,
    #                        secondaryjoin=id==Friendship.friend_b_id)

    # def befriend(self, friend):
    #     if friend not in self.friends:
    #         self.friends.append(friend)
    #         friend.friends.append(self)

    # def unfriend(self, friend):
    #     if friend in self.friends:
    #         self.friends.remove(friend)
    #         friend.friends.remove(self)

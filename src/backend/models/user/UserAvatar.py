from flask_login import UserMixin

from dataclasses import dataclass
from app import db, login_manager    
from typing import List
from sqlalchemy import and_, func, or_
from marshmallow import Schema, fields
from flask import redirect
from models.user.User import User

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
@dataclass
class UserAvatar(db.Model):
    __tablename__ = "user_avatar"

    id : int
    title : str
    image_location : str
    
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    title = db.Column(db.String(50), nullable=False, unique=True)
    image_location = db.Column(db.String(200), nullable=False)
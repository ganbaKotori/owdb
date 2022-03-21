from http import server
from flask_login import LoginManager, UserMixin, login_required, login_user, current_user, logout_user

from dataclasses import dataclass
from sqlalchemy import Enum, select

from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager
import api.match.models, api.map.models                             

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

@dataclass
class User(UserMixin, db.Model):
    __tablename__ = "user"
    id : int
    email : str
    
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    username = db.Column(db.String(12), unique=True)
    password = db.Column(db.String(256), server_default='')

    matches = db.relationship('Match', backref='original_user')

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


from flask_login import UserMixin

from dataclasses import dataclass
from app import db, login_manager    
from typing import List
from sqlalchemy import and_, func, or_
from marshmallow import Schema, fields
from flask import redirect
from routes.api.match.models import Match, MatchUser

# @dataclass
# class Friendship(db.Model):
#     __tablename__ = "friendship"
    
#     friend_a_id = db.Column(db.Integer, primary_key=True)
#     friend_b_id = db.Column(db.Integer, primary_key=True)

#     __table_args__ = (db.ForeignKeyConstraint(
#                             ['friend_a_id', 'friend_b_id'], 
#                             ['user.id', 'user.id']), 
#                   )

class UserSchema(Schema):
    username = fields.String()
    
class FriendshipSchema(Schema):
    id = fields.Integer()
    user = fields.Nested(UserSchema)

class Friendship(db.Model):
    __tablename__ = 'friendship'
    user_id = db.Column(db.ForeignKey('user.id') , autoincrement=False,primary_key=True)
    friend_id = db.Column(db.ForeignKey('user.id'), autoincrement=False, primary_key=True)
    id = db.Column(db.Integer, autoincrement=True, primary_key=False, unique=True, nullable=False)

    request_accepted = db.Column(db.Boolean, nullable=False, default=False)

    user = db.relationship('User',primaryjoin="User.id == Friendship.user_id")


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect('/login')

@dataclass
class User(UserMixin, db.Model):
    __tablename__ = "user"
    id : int
    email : str
    username : str
    requested_friends : List[Friendship]
    requested_friends : List[Friendship]
    
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(256), server_default='')

    matches = db.relationship('Match', backref='original_user')

    requested_friends = db.relationship('Friendship',backref='to', primaryjoin=id==Friendship.user_id)
    receieved_friends = db.relationship('Friendship',backref='from', primaryjoin=id==Friendship.friend_id)

    user_avatar_id = db.Column(db.Integer, db.ForeignKey('user_avatar.id'),default=0) #NOTE: this may not work
    user_avatar_image = db.relationship("UserAvatar")

    def send_friend_request(self, requested_friend_id):
        self.requested_friends.append(Friendship(user_id=self.id, friend_id=requested_friend_id))

    def accept_friend_request(self, friendship_id):
        friendship = Friendship.query.filter(and_(Friendship.id==friendship_id, Friendship.friend_id==self.id, Friendship.request_accepted==False)).first()
        friendship.request_accepted = True

    def decline_friend_request(self, friendship_id):
        friendship = Friendship.query.filter(and_(Friendship.id==friendship_id, Friendship.friend_id==self.id, Friendship.request_accepted==False)).first()
        db.session.delete(friendship)

    def remove_friend(self, friendship_id):
        friendship = Friendship.query.filter(and_(Friendship.id==friendship_id, Friendship.friend_id==self.id, Friendship.request_accepted==True)).first()
        db.session.delete(friendship)

    def remove_friend_by_username(self, friend_username):
        friend = User.query.filter(User.username==friend_username).first_or_404()
        friendship = Friendship.query.filter(or_(
                                                    and_(Friendship.user_id==friend.id, Friendship.friend_id==self.id, Friendship.request_accepted==True),
                                                    and_(Friendship.user_id==self.id, Friendship.friend_id==friend.id, Friendship.request_accepted==True),
                                                )).first_or_404()
        db.session.delete(friendship)

    def get_friend_requests(self):
        pending_requests = Friendship.query.filter(and_(Friendship.friend_id==self.id, Friendship.request_accepted==False)).all()
        pr_dict_list = []
        for p in pending_requests:
            friendship_schema = FriendshipSchema()
            friendship_dict = friendship_schema.dump(p)
            pr_dict_list.append(friendship_dict)
        return pr_dict_list

    def get_match_invite_count(self):
        k = db.session.execute(
                    db.session
                        .query(Match)
                        .join(MatchUser, Match.users)
                        .filter(MatchUser.user_id == self.id)
                        .filter(MatchUser.accepted_flag == False)
                        .statement.with_only_columns([func.count()]).order_by(None)
                    ).scalar()
        return k

    def get_friend_request_count(self):
        k = db.session.execute(
                    db.session
                        .query(Friendship)
                        .filter(Friendship.friend_id == self.id)
                        .filter(Friendship.request_accepted == False)
                        .statement.with_only_columns([func.count()]).order_by(None)
                    ).scalar()
        return k



    

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

@dataclass
class UserAvatar(db.Model):
    __tablename__ = "user_avatar"

    id : int
    title : str
    image_location : str
    
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    title = db.Column(db.String(50), nullable=False, unique=True)
    image_location = db.Column(db.String(200), nullable=False)


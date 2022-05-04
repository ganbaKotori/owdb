from flask import render_template, redirect, url_for, Blueprint
from flask_login import login_required, current_user

friend = Blueprint('friend', __name__)

@friend.get('/friends')
@login_required
def get_friends_page():
    return render_template('user/all_friends.html')

@friend.get('/add_friend')
@login_required
def get_add_friend_page():
    return render_template('user/add_friend.html')

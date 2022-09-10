from flask import render_template, redirect, url_for, Blueprint
from flask_login import login_required, current_user
import api.user.utils as utils

friend = Blueprint('friend', __name__)

@friend.get('/friends')
@login_required
def get_friends_page():
    current_user_friends = utils.get_current_user_friends()
    return render_template('user/all_friends.html', current_user_friends=current_user_friends)

# @friend.get('/add_friend')
# @login_required
# def get_add_friend_page():
#     return render_template('user/add_friend.html')

# @friend.get('/pending')
# @login_required
# def get_pending_requests_page():
#     current_user_pending_friend_requests = utils.get_current_user_pending_friend_requests()
#     return render_template('user/all_friends.html', current_user_friends=current_user_pending_friend_requests)
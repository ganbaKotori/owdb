from flask import render_template, redirect, url_for, Blueprint
from flask_login import login_required, current_user


user = Blueprint('user', __name__, url_prefix='/user')


@user.get('/friends')
@login_required
def get_friends_page():
    return 'YOU HAVE NO FRIENDS!!!'

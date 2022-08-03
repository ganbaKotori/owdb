from flask import render_template, redirect, url_for, Blueprint
from flask_login import login_required, current_user

user = Blueprint('user', __name__)

@user.get('/<string:username>')
@login_required
def get_user_profile_page(username):
    return render_template('user/user_profile.html', user=user)



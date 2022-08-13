from flask import render_template, redirect, url_for, Blueprint
from flask_login import login_required, current_user

from api.match.models import Match
from api.user.models import User
from sqlalchemy import desc


user = Blueprint('user', __name__, url_prefix='/u')

@user.get('/<string:username>')
def get_user_profile_page(username):
    user = User.query.filter(User.username==username).first_or_404()
    current_user_matches = Match.query.filter(Match.created_by_user_id==user.id).order_by(desc(Match.date_match_played)).limit(5).all()
    return render_template('user/user_profile.html', user=user, current_user_matches=current_user_matches, is_user_friends=False)



from flask import render_template, redirect, url_for, Blueprint
from flask_login import login_required, current_user

from api.match.models import Match
from api.user.models import User
import api.user.utils as user_utils
from sqlalchemy import desc


user = Blueprint('user', __name__, url_prefix='/u')

@user.get('/<string:username>')
def get_user_profile_page(username):
    user = User.query.filter(User.username==username).first_or_404()
    relationship_status = user_utils.get_current_user_relationship_status(user.id)
    current_user_matches = Match.query.filter(Match.created_by_user_id==user.id).order_by(desc(Match.date_match_played)).limit(5).all()
    return render_template('user/user_profile.html', user=user, current_user_matches=current_user_matches,relationship_status=relationship_status)



from flask import render_template, redirect, url_for, Blueprint
from flask_login import login_required, current_user

from api.match.models import Match
from api.user.models import User
import api.user.utils as user_utils
import api.match.utils as match_utils
from sqlalchemy import desc


user = Blueprint('user', __name__, url_prefix='/u')

@user.get('/<string:username>')
def get_user_profile_page(username):
    user = User.query.filter(User.username==username).first_or_404()

    all_matches = match_utils.get_current_user_matches(match_count=5, user_id=user.id)
    is_current_user_profile = False
    if current_user.is_authenticated:
        relationship_status = user_utils.get_current_user_relationship_status(user.id)
        if current_user.id == user.id:
            is_current_user_profile = True
    else:
        relationship_status = None

    return render_template('user/user_profile.html', 
                            user=user, 
                            current_user_matches=all_matches,
                            relationship_status=relationship_status,
                            is_current_user_profile=is_current_user_profile)



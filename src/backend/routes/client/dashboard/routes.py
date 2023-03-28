from flask import render_template, Blueprint
from flask_login import login_required, current_user
from models.match.Match import Match
from models.user.User import User
from app import db
from sqlalchemy import desc
import routes.api.match.utils as match_utils


dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/dashboard')
@login_required
def user_dashboard():
    # current_user.send_friend_request(7)
    # db.session.commit()
    #current_user_matches = Match.query.filter(Match.created_by_user_id==current_user.id).order_by(desc(Match.date_match_played)).limit(5).all()
    #print(current_user_matches)
    recent_matches = match_utils.get_current_user_matches(match_count=10, user_id=current_user.id)
    return render_template('home/dashboard.html', current_user_matches=recent_matches)
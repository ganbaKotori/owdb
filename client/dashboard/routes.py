from flask import render_template, Blueprint
from flask_login import login_required, current_user
from api.match.models import Match
from api.user.models import User
from app import db
from sqlalchemy import desc


dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/dashboard')
@login_required
def user_dashboard():
    # current_user.send_friend_request(7)
    # db.session.commit()
    current_user_matches = Match.query.filter(Match.created_by_user_id==current_user.id).order_by(desc(Match.date_match_played)).limit(5).all()
    print(current_user_matches)
    return render_template('home/dashboard.html', current_user_matches=current_user_matches)
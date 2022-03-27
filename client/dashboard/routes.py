from flask import render_template, Blueprint
from flask_login import login_required, current_user
from api.match.models import Match

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/dashboard')
@login_required
def user_dashboard():
    current_user_matches = Match.query.filter(Match.user_id==current_user.id).all()
    print(current_user_matches)
    return render_template('home/dashboard.html', current_user_matches=current_user_matches)
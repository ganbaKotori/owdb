from flask import render_template, Blueprint
from flask_login import login_required

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/dashboard')
@login_required
def user_dashboard():
    return render_template('home/dashboard.html')
from flask import render_template, redirect, url_for, Blueprint
from flask_login import login_required, logout_user
from api.map.models import Map

match = Blueprint('match', __name__, url_prefix='/match')

@match.get('/create')
def get_create_match_page():
    return render_template('match/create_match.html')
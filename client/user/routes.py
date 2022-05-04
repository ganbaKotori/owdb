from flask import render_template, redirect, url_for, Blueprint
from flask_login import login_required, current_user

user = Blueprint('user', __name__)

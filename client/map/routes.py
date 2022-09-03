from urllib import request
from flask import render_template, redirect, url_for, Blueprint
from flask_login import login_required, current_user
from api.map.models import Map
from api.hero.models import Hero, HeroRole
from api.match.models import Match, MatchUser, MatchUserHero, Hero
from api.match.forms import CreateMatchForm
import api.user.utils as user_utils
from app import db
from sqlalchemy.orm import joinedload
from api.user.models import User

ow_map = Blueprint('ow_map', __name__, url_prefix='/map')
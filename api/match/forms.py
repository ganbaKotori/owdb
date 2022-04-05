from flask_wtf import FlaskForm, Form
from wtforms import StringField, FormField, FieldList, IntegerField, SelectField, RadioField
from wtforms.validators import Optional


class MatchRound(Form):
    #result = RadioField(u'Match Result', choices=[('All Objectives Cleared', 'Success'), ('Out of Time', 'Fail')])
    phase = RadioField(u'Match Phase', choices=[('ATTACK', 'ATTACK'), ('DEFEND', 'DEFEND')])

class CreateMatchForm(FlaskForm):
    match_rounds = FieldList(FormField(MatchRound), min_entries=1, max_entries=10)
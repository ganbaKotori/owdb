from dataclasses import Field
from flask_wtf import FlaskForm, Form
from wtforms import StringField, FormField, FieldList, IntegerField, SelectField, RadioField
from wtforms.validators import Optional, NumberRange


class MatchRound(Form):
    #result = RadioField(u'Match Result', choices=[('All Objectives Cleared', 'Success'), ('Out of Time', 'Fail')])
    phase = RadioField(u'Match Phase', choices=[('ATTACK', 'Attack'), ('DEFEND', 'Defend')])
    score = IntegerField('Score', [NumberRange(min=0, max=100)])

class TaggedUser(Form):
    role = RadioField(u'Role', choices=[('DAMAGE', 'Damage'), ('TANK', 'Tank'),('SUPPORT', 'Support')])
    username = SelectField('Friend', choices=[""])
    #NOTE: when validating friends, you need to iterate through tagged_friends because it is a fieldlist thus it will be a list!
    #TODO: use hero roles' id instead of hardcoded strings!

class CreateMatchForm(FlaskForm):
    match_rounds = FieldList(FormField(MatchRound), min_entries=1, max_entries=10)
    tagged_friends = FieldList(FormField(TaggedUser), min_entries=0, max_entries=5)

class EditMatchForm(FlaskForm):
    #match_rounds = FieldList(FormField(MatchRound), min_entries=1, max_entries=10)
    tagged_friends = FieldList(FormField(TaggedUser), min_entries=0, max_entries=5)
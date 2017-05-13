from flask_wtf import Form
from wtforms import StringField, SubmitField, SelectField, IntegerField, FloatField, BooleanField, \
    DateField, validators


class UserSpecificExerciseForm(Form):
    exercise = SelectField(label='Which exercise history do you want to see?')
    submit = SubmitField()


class AddRepHistoryForm(Form):
    exercise = SelectField(label="Which exercise did you do?")
    sets = IntegerField(label='How many sets did you do?', validators=[validators.DataRequired()])
    reps = IntegerField(label='How many reps of each set did you do?', validators=[validators.DataRequired()])
    weight = FloatField(label='What weight did you use?', validators=[validators.DataRequired()])
    exercise_date = DateField(label='When was this?', validators=[validators.DataRequired()])
    submit = SubmitField()


class AddRepTaxonomyForm(Form):
    name = StringField(label='What is the name of the exercise?', validators=[validators.DataRequired()])
    is_back = BooleanField(label='For back:')
    is_chest = BooleanField(label='For chest:')
    is_shoulders = BooleanField(label='For shoulders:')
    is_biceps = BooleanField(label='For biceps:')
    is_triceps = BooleanField(label='For triceps:')
    is_legs = BooleanField(label='For legs:')
    is_core = BooleanField(label='For core:')
    is_balance = BooleanField(label='For balance:')
    is_cardio = BooleanField(label='For cardio:')
    is_weight_per_hand = BooleanField(label='Is weight per hand:')
    submit = SubmitField()

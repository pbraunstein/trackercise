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

from flask_wtf import Form
from wtforms import SubmitField, SelectField


class UserSpecificExerciseForm(Form):
    exercise = SelectField(label='Which exercise history do you want to see?')
    submit = SubmitField()

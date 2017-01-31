from flask_wtf import Form
from wtforms import (StringField, PasswordField, SubmitField, SelectField, IntegerField, FloatField, DateField,\
    validators)


class UserForm(Form):
    email = StringField(label="Enter Your Email", validators=[validators.DataRequired()])
    submit = SubmitField()


class LoginForm(UserForm):
    password = PasswordField(label="Enter Your Password", validators=[validators.DataRequired()])


class RegisterForm(UserForm):
    nickname = StringField(label="What do you like to be called?", validators=[validators.DataRequired()])
    password = PasswordField(label="Create a Password", validators=[validators.DataRequired()])


class AddRepHistoryForm(Form):
    exercise = SelectField(label="Which exercise did you do?")
    sets = IntegerField(label='How many sets did you do?', validators=[validators.DataRequired()])
    reps = IntegerField(label='How many reps of each set did you do?', validators=[validators.DataRequired()])
    weight = FloatField(label='What weight did you use?', validators=[validators.DataRequired()])
    date = DateField(label='When was this?', validators=[validators.DataRequired()])
    submit = SubmitField()

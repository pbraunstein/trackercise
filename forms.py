from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, validators


class LoginForm(Form):
    username = StringField(label="Enter Your Username", validators=[validators.DataRequired()])
    password = PasswordField(label="Enter Your Password", validators=[validators.DataRequired()])
    submit = SubmitField()

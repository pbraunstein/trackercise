from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, validators


class LoginForm(Form):
    username = StringField(label="Enter Your Username", validators=[validators.DataRequired()])
    password = PasswordField(label="Enter Your Password", validators=[validators.DataRequired()])
    submit = SubmitField()


class RegisterForm(Form):
    username = StringField(label="Enter Your Email Address", validators=[validators.DataRequired()])
    password = PasswordField(label="Create a Password", validators=[validators.DataRequired()])
    submit = SubmitField()

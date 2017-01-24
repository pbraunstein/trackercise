from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, validators


class UserForm(Form):
    email = StringField(label="Enter Your Email", validators=[validators.DataRequired()])
    submit = SubmitField()


class LoginForm(UserForm):
    password = PasswordField(label="Enter Your Password", validators=[validators.DataRequired()])


class RegisterForm(UserForm):
    password = PasswordField(label="Create a Password", validators=[validators.DataRequired()])

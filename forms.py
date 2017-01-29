from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, SelectField, validators


class UserForm(Form):
    email = StringField(label="Enter Your Email", validators=[validators.DataRequired()])
    submit = SubmitField()


class LoginForm(UserForm):
    password = PasswordField(label="Enter Your Password", validators=[validators.DataRequired()])


class RegisterForm(UserForm):
    nickname = StringField(label="What do you like to be called?", validators=[validators.DataRequired()])
    password = PasswordField(label="Create a Password", validators=[validators.DataRequired()])


class AddRepHistoryForm(Form):
    exercise = SelectField(
        label="Which exercise did you do?",
    )

from wtforms import Form, StringField, PasswordField, validators


class LoginForm(Form):
    username = StringField(label="Username", validators=[validators.DataRequired()])
    password = PasswordField(label="Password", validators=[validators.DataRequired()])

import os

from flask import Flask, render_template, redirect
from flask import flash
from flask_login import LoginManager, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy

from forms import LoginForm, RegisterForm

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

# These are here to avoid circular imports
from brain.admin.all_data import AllData
from brain.custom_exceptions import ThisShouldNeverHappenException
from brain.user_management.loginerator import Loginerator
from brain.user_management.login_results import LoginResults
from brain.user_management.register_city import RegisterCity
from brain.user_management.register_results import RegisterResults
from models import Users, RepExercisesHistory, RepExercisesTaxonomy


@app.route('/')
@login_required
def index():
    return render_template('index.html', entries=AllData.get_all_data())


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        login_result = Loginerator.login(form.email.data, form.password.data)
        if login_result == LoginResults.NO_SUCH_USER:
            flash('We do not have a user of that username')
        elif login_result == LoginResults.INCORRECT_PASSWORD:
            flash('Incorrect password')
        elif login_result == LoginResults.LOGGED_IN:
            flash('Successful Login')
            return redirect('/')
        else:
            raise ThisShouldNeverHappenException("Invalid LoginResult Returned {0}".format(login_result))
    return render_template('login.html', form=form)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    flash('You have been logged out')
    logout_user()
    return redirect('/login')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        reg_result = RegisterCity.register(form.email.data, form.nickname.data, form.password.data)
        if reg_result == RegisterResults.INVALID_EMAIL:
            flash('Email not valid')
        elif reg_result == RegisterResults.EMAIL_ALREADY_EXISTS:
            flash('Email already exists')
        elif reg_result == RegisterResults.REGISTERED:
            flash('New user registered successfully')
            return redirect('/login')
        else:
            raise ThisShouldNeverHappenException("Invalid RegisterResult Returned {0}".format(reg_result))
    return render_template('register.html', form=form)


@login_manager.user_loader
def user_loader(user_email):
    return Users.query.get(user_email)


if __name__ == '__main__':
    app.run()

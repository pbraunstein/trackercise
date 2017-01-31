import os

from flask import Flask, render_template, redirect
from flask import flash
from flask_login import LoginManager, logout_user, login_required, current_user
from flask_sqlalchemy import SQLAlchemy

from forms import LoginForm, RegisterForm, AddRepHistoryForm

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

# These are here to avoid circular imports
from brain.admin.all_data import AllData
from brain.admin.user_data import UserData
from brain.custom_exceptions import ThisShouldNeverHappenException
from brain.exercises_management.rep_exercises_management import RepExercisesManagement
from brain.user_management.loginerator import Loginerator
from brain.user_management.login_result import LoginResult
from brain.user_management.register_city import RegisterCity
from brain.user_management.register_result import RegisterResult
from models import Users, RepExercisesHistory, RepExercisesTaxonomy


@login_required
def all_data():
    return render_template('all_data.html', entries=AllData.get_all_data())


@app.route('/')
@login_required
def user_data():
    return render_template('user_data.html', context=UserData.get_user_data())


@app.route('/add-rep-history', methods=['GET', 'POST'])
@login_required
def add_rep_history():
    form = AddRepHistoryForm()
    form.exercise.choices = RepExercisesManagement.get_valid_id_exercise_pairs()
    if form.validate_on_submit():
        entry_added = RepExercisesManagement.submit_history_entry(
            user_id=current_user.id,
            exercise_id=form.exercise.data,
            sets=form.sets.data,
            reps=form.reps.data,
            weight=form.weight.data,
            exercise_date=form.exercise_date.data
        )
        flash('you just logged exercise_id={0}, sets={1}, reps{2}, weight{3}'.format(
            entry_added.exercise_id,
            entry_added.sets,
            entry_added.reps,
            entry_added.weight
        ))
        return redirect('/')
    return render_template('add_rep_history.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        login_result = Loginerator.login(form.email.data, form.password.data)
        if login_result == LoginResult.NO_SUCH_USER:
            flash('We do not have a user of that username')
        elif login_result == LoginResult.INCORRECT_PASSWORD:
            flash('Incorrect password')
        elif login_result == LoginResult.LOGGED_IN:
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
        if reg_result == RegisterResult.INVALID_EMAIL:
            flash('Email not valid')
        elif reg_result == RegisterResult.EMAIL_ALREADY_EXISTS:
            flash('Email already exists')
        elif reg_result == RegisterResult.REGISTERED:
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

import hashlib
import os

from flask import Flask, render_template, redirect
from flask import flash
from flask_login import LoginManager, login_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy

from forms import LoginForm, RegisterForm

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


from models import Users, RepExercisesHistory, RepExercisesTaxonomy


@app.route('/')
@login_required
def index():
    user_results = list(Users.query.all())
    taxonomy_results = list(RepExercisesTaxonomy.query.all())
    taxonomy_results = [_prepare_taxonomy_entry(x) for x in taxonomy_results]
    history_results = list(RepExercisesHistory.query.all())
    history_results = [_prepare_history_entry(x) for x in history_results]
    entries = [user_results, taxonomy_results, history_results]

    return render_template('index.html', entries=entries)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.get(form.email.data)
        inputted_password_hash = hashlib.sha256(form.password.data).hexdigest()
        if user is None:
            flash('We do not have a user whose email is {0}'.format(form.username.data))
        elif inputted_password_hash != user.password:
            flash('Incorrect password')
        else:
            flash('Successful Login')
            login_user(user)
            return redirect('/')
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
        flash("YES")
    else:
        flash("NO")
    return render_template('register.html', form=form)


@login_manager.user_loader
def user_loader(user_email):
    return Users.query.get(user_email)


def _prepare_history_entry(entry):
    """
    Stringifies date of RepExercisesHistory entry
    """
    entry.date = str(entry.date)
    return entry


def _prepare_taxonomy_entry(entry):
    """
    Turns boolean True or False to YES or NO for RepExercisesTaxonomy entry
    """
    def debooleanize(value):
        return 'YES' if value else 'NO'

    entry.is_back = debooleanize(entry.is_back)
    entry.is_chest = debooleanize(entry.is_chest)
    entry.is_shoulders = debooleanize(entry.is_shoulders)
    entry.is_biceps = debooleanize(entry.is_biceps)
    entry.is_triceps = debooleanize(entry.is_triceps)
    entry.is_legs = debooleanize(entry.is_legs)
    entry.is_core = debooleanize(entry.is_core)
    entry.is_balance = debooleanize(entry.is_balance)
    entry.is_cardio = debooleanize(entry.is_cardio)
    entry.is_weight_per_hand = debooleanize(entry.is_weight_per_hand)

    return entry


if __name__ == '__main__':
    app.run()

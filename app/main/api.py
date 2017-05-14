from json import dumps
from random import randint
from os.path import dirname, join

from flask import flash, redirect, render_template, send_file, request
from flask_login import login_required, current_user

from app.brain.admin.all_data import AllData
from app.brain.admin.user_data import UserData
from app.brain.custom_exceptions import ThisShouldNeverHappenException
from app.brain.exercises_management.rep_exercises_management import RepExercisesManagement
from app.brain.user_management.loginerator import Loginerator
from app.brain.user_management.login_result import LoginResult
from app.brain.user_management.register_city import RegisterCity
from app.brain.user_management.register_result import RegisterResult
from app.brain.utilities import all_data_to_dict, user_data_to_dict
from app.constants import TAXONOMY_CONSTANTS
from app.main import main_blueprint as main
from app.main.forms import AddRepHistoryForm, UserSpecificExerciseForm


@main.route('/')
def ts():
    serve_path = dirname(main.root_path)
    serve_path = join(serve_path, 'static')
    serve_path = join(serve_path, 'dist')
    serve_path = join(serve_path, 'index.html')
    return send_file(serve_path)


@main.route('/get-rand-num')
def get_rand_num():
    results = {'num': randint(1, 101)}
    return dumps(results)


@main.route('/all-data')
def all_data():
    return dumps(all_data_to_dict(AllData.get_all_data()))


@main.route('/status')
def status():
    return dumps({'status': 'good'})


@main.route('/user-data')
def user_data():
    if not current_user.is_authenticated:
        return dumps({'status': 'bad'})
    return dumps(user_data_to_dict(UserData.get_user_data()))


@main.route('/history-by-taxonomy', methods=['GET', 'POST'])
@login_required
def history_by_taxonomy():
    form = UserSpecificExerciseForm()
    form.exercise.choices = RepExercisesManagement.get_valid_id_exercise_pairs()
    context = {
        'form': form,
        'nickname': current_user.nickname,
        'history': []
    }

    if form.validate_on_submit():
        context = {
            'form': form,
            'nickname': current_user.nickname,
            'history': RepExercisesManagement.get_user_history_by_exercise_id(
                user_id=current_user.id,
                exercise_id=int(form.exercise.data)
            )
        }

    return render_template('history_by_taxonomy.html', context=context)


@main.route('/add-rep-history', methods=['GET', 'POST'])
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
        flash('you just logged exercise_id={0}, sets={1}, reps={2}, weight={3}, date={4}'.format(
            entry_added.exercise_id,
            entry_added.sets,
            entry_added.reps,
            entry_added.weight,
            entry_added.date
        ))
        return redirect('/')
    return render_template('add_rep_history.html', form=form)


@main.route('/add-rep-taxonomy', methods=['GET', 'POST'])
def add_rep_taxonomy():
    if not request.args.get(TAXONOMY_CONSTANTS.NAME):  # This is the only required field
        return dumps({'status': 'bad'})

    RepExercisesManagement.submit_taxonomy_entry(
        name=request.args.get(TAXONOMY_CONSTANTS.NAME).upper(),
        is_back=RepExercisesManagement.convert_ts_strings_to_booleans(request.args.get(TAXONOMY_CONSTANTS.IS_BACK)),
        is_chest=RepExercisesManagement.convert_ts_strings_to_booleans(request.args.get(TAXONOMY_CONSTANTS.IS_CHEST)),
        is_shoulders=RepExercisesManagement.convert_ts_strings_to_booleans(
            request.args.get(TAXONOMY_CONSTANTS.IS_SHOULDERS)
        ),
        is_biceps=RepExercisesManagement.convert_ts_strings_to_booleans(request.args.get(TAXONOMY_CONSTANTS.IS_BICEPS)),
        is_triceps=RepExercisesManagement.convert_ts_strings_to_booleans(
            request.args.get(TAXONOMY_CONSTANTS.IS_TRICEPS)
        ),
        is_legs=RepExercisesManagement.convert_ts_strings_to_booleans(request.args.get(TAXONOMY_CONSTANTS.IS_LEGS)),
        is_core=RepExercisesManagement.convert_ts_strings_to_booleans(request.args.get(TAXONOMY_CONSTANTS.IS_CORE)),
        is_balance=RepExercisesManagement.convert_ts_strings_to_booleans(
            request.args.get(TAXONOMY_CONSTANTS.IS_BALANCE)
        ),
        is_cardio=RepExercisesManagement.convert_ts_strings_to_booleans(request.args.get(TAXONOMY_CONSTANTS.IS_CARDIO)),
        is_weight_per_hand=RepExercisesManagement.convert_ts_strings_to_booleans(
            request.args.get(TAXONOMY_CONSTANTS.IS_WEIGHT_PER_HAND)
        )
    )
    return dumps({'status': 'good'})


@main.route('/login', methods=['GET', 'POST'])
def login():
    email = request.args.get('email')
    password = request.args.get('password')
    login_result = Loginerator.login(email, password)
    if login_result == LoginResult.LOGGED_IN:
        return dumps({
            'status': 'good',
            'user_logged_in': current_user.nickname
        })
    else:
        return dumps({'status': 'bad'})


@main.route('/who-am-i', methods=['GET', 'POST'])
def who_am_i():
    if current_user.is_authenticated:
        return dumps({
            'user': current_user.nickname
        })
    else:
        return dumps({
            'user': ''
        })


@main.route('/logout', methods=['GET', 'POST'])
def logout():
    Loginerator.logout()
    return dumps({})


@main.route('/register', methods=['GET', 'POST'])
def register():
    email = request.args.get('email')
    nickname = request.args.get('nickname')
    password = request.args.get('password')
    reg_result = RegisterCity.register(email, nickname, password)
    if reg_result == RegisterResult.REGISTERED:
        return dumps({'status': 'good'})
    else:
        return dumps({'status': 'bad'})

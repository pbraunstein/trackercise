from json import dumps
from os.path import dirname, join

from flask import send_file, request, g, Response
from flask_login import current_user
from flask_wtf.csrf import generate_csrf

from app import csrf
from app.brain.admin.all_data import AllData
from app.brain.admin.user_data import UserData
from app.brain.exercises_management.rep_exercises_management import RepExercisesManagement
from app.brain.exercises_management.time_exercises_management import TimeExercisesManagement
from app.brain.user_management.account_updater import AccountUpdater
from app.brain.user_management.change_password_result import ChangePasswordResult
from app.brain.user_management.loginerator import Loginerator
from app.brain.user_management.login_result import LoginResult
from app.brain.user_management.register_city import RegisterCity
from app.brain.user_management.register_result import RegisterResult
from app.brain.utilities import all_data_to_dict, user_data_to_dict, list_history_objs_to_dicts
from app.constants import TAXONOMY_CONSTANTS, HISTORY_CONSTANTS
from app.main import main_blueprint as main


@main.route('/')
def ts():
    serve_path = dirname(main.root_path)
    serve_path = join(serve_path, 'static')
    serve_path = join(serve_path, 'dist')
    serve_path = join(serve_path, 'index.html')
    return send_file(serve_path), 200


@main.route('/all-data', methods=['POST'])
def all_data():
    return dumps(all_data_to_dict(AllData.get_all_data())), 200


@main.route('/status', methods=['GET', 'POST'])
def status():
    return dumps({'status': 'good'}), 200


@main.route('/user-data', methods=['POST'])
def user_data():
    csrf.protect()
    if not current_user.is_authenticated:
        return dumps({'status': 'bad'}), 400
    return dumps(user_data_to_dict(UserData.get_user_data())), 200


@main.route('/history-by-taxonomy', methods=['POST'])
def history_by_taxonomy():
    csrf.protect()
    if not current_user.is_authenticated:
        return dumps({'status': 'bad'}), 400

    parameters = request.get_json()

    history = RepExercisesManagement.get_user_history_by_exercise_id(
        user_id=current_user.id,
        exercise_id=parameters.get('exercise_id')
    )

    return dumps({
        'status': 'good',
        'nickname': current_user.nickname,
        'history': list_history_objs_to_dicts(history)
    }), 200


@main.route('/history-by-date', methods=['POST'])
def history_by_date():
    csrf.protect()
    if not current_user.is_authenticated:
        return dumps({'status': 'bad'}), 400

    parameters = request.get_json()

    history = RepExercisesManagement.get_user_history_by_date(
        user_id=current_user.id,
        exercise_date=parameters.get('exercise_date')
    )

    return dumps({
        'status': 'good',
        'nickname': current_user.nickname,
        'history': list_history_objs_to_dicts(history)
    }), 200


@main.route('/add-rep-history', methods=['POST'])
def add_rep_history():
    if not current_user.is_authenticated:
        return dumps({'status': 'bad'}), 400

    parameters = request.get_json()

    RepExercisesManagement.submit_history_entry(
        user_id=current_user.id,
        exercise_id=parameters.get(HISTORY_CONSTANTS.EXERCISE_ID),
        sets=parameters.get(HISTORY_CONSTANTS.SETS),
        reps=parameters.get(HISTORY_CONSTANTS.REPS),
        weight=parameters.get(HISTORY_CONSTANTS.WEIGHT),
        exercise_date=parameters.get(HISTORY_CONSTANTS.DATE)
    )
    return dumps({'status': 'good'}), 200


@main.route('/add-time-history', methods=['POST'])
def add_time_history():
    if not current_user.is_authenticated:
        return dumps({'status': 'bad'}), 400

    parameters = request.get_json()

    return dumps({'status': 'good'}), 200


@main.route('/get-valid-id-exercise-pairs', methods=['POST'])
def get_valid_id_exercise_pairs():
    return dumps({
        'pairs': RepExercisesManagement.get_valid_id_exercise_pairs()
    }), 200


@main.route('/add-rep-taxonomy', methods=['POST'])
def add_rep_taxonomy():
    parameters = request.get_json()

    if not parameters.get(TAXONOMY_CONSTANTS.NAME):  # This is the only required field
        return dumps({'status': 'bad'}), 400

    RepExercisesManagement.submit_taxonomy_entry(
        name=parameters.get(TAXONOMY_CONSTANTS.NAME).upper(),
        is_back=RepExercisesManagement.convert_ts_strings_to_booleans(parameters.get(TAXONOMY_CONSTANTS.IS_BACK)),
        is_chest=RepExercisesManagement.convert_ts_strings_to_booleans(parameters.get(TAXONOMY_CONSTANTS.IS_CHEST)),
        is_shoulders=RepExercisesManagement.convert_ts_strings_to_booleans(
            parameters.get(TAXONOMY_CONSTANTS.IS_SHOULDERS)
        ),
        is_biceps=RepExercisesManagement.convert_ts_strings_to_booleans(parameters.get(TAXONOMY_CONSTANTS.IS_BICEPS)),
        is_triceps=RepExercisesManagement.convert_ts_strings_to_booleans(
            parameters.get(TAXONOMY_CONSTANTS.IS_TRICEPS)
        ),
        is_legs=RepExercisesManagement.convert_ts_strings_to_booleans(parameters.get(TAXONOMY_CONSTANTS.IS_LEGS)),
        is_core=RepExercisesManagement.convert_ts_strings_to_booleans(parameters.get(TAXONOMY_CONSTANTS.IS_CORE)),
        is_balance=RepExercisesManagement.convert_ts_strings_to_booleans(
            parameters.get(TAXONOMY_CONSTANTS.IS_BALANCE)
        ),
        is_cardio=RepExercisesManagement.convert_ts_strings_to_booleans(parameters.get(TAXONOMY_CONSTANTS.IS_CARDIO)),
        is_weight_per_hand=RepExercisesManagement.convert_ts_strings_to_booleans(
            parameters.get(TAXONOMY_CONSTANTS.IS_WEIGHT_PER_HAND)
        )
    )
    return dumps({'status': 'good'}), 200


@main.route('/add-time-taxonomy', methods=['POST'])
def add_time_taxonomy():
    parameters = request.get_json()

    if not parameters.get(TAXONOMY_CONSTANTS.NAME):  # This is the only required field
        return dumps({'status': 'bad'}), 400

    TimeExercisesManagement.submit_taxonomy_entry(parameters.get(TAXONOMY_CONSTANTS.NAME))

    return dumps({'status': 'good'}), 200


@main.route('/login', methods=['POST'])
def login():
    parameters = request.get_json()
    email = parameters.get('email')
    password = parameters.get('password')
    login_result = Loginerator.login(email, password)
    if login_result == LoginResult.LOGGED_IN:
        response = Response(dumps({
            'status': 'good',
            'user_logged_in': current_user.nickname
        }))
        generate_csrf()
        response.headers['X-CSRFToken'] = getattr(g, 'csrf_token')
        return response, 200
    else:
        return dumps({'status': 'bad'}), 400


@main.route('/who-am-i', methods=['POST'])
def who_am_i():
    if current_user.is_authenticated:
        return dumps({
            'user': current_user.nickname,
            'password': current_user.password
        }), 200
    else:
        return dumps({
            'user': ''
        }), 200


@main.route('/logout', methods=['POST'])
def logout():
    Loginerator.logout()
    return dumps({}), 200


@main.route('/register', methods=['POST'])
def register():
    parameters = request.get_json()
    email = parameters.get('email')
    nickname = parameters.get('nickname')
    password = parameters.get('password')
    reg_result = RegisterCity.register(email, nickname, password)
    if reg_result == RegisterResult.REGISTERED:
        return dumps({'status': 'good'}), 200
    else:
        return dumps({'status': 'bad'}), 400


@main.route('/change-password', methods=['POST'])
def change_password():
    if not current_user.is_authenticated:
        return dumps({'status': 'bad'}), 400

    parameters = request.get_json()
    old_password = parameters.get('old_password')
    new_password = parameters.get('new_password')
    confirm_password = parameters.get('confirm_password')
    change_password_result = AccountUpdater.change_password(old_password, new_password, confirm_password)

    if change_password_result == ChangePasswordResult.PASSWORD_CHANGE_SUCCESSFUL:
        return dumps({'status': 'good'}), 200
    else:
        return dumps({'status': 'bad'}), 400

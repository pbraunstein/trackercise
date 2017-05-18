from json import dumps
from os.path import dirname, join

from flask import send_file, request
from flask_login import current_user

from app.brain.admin.all_data import AllData
from app.brain.admin.user_data import UserData
from app.brain.exercises_management.rep_exercises_management import RepExercisesManagement
from app.brain.user_management.loginerator import Loginerator
from app.brain.user_management.login_result import LoginResult
from app.brain.user_management.register_city import RegisterCity
from app.brain.user_management.register_result import RegisterResult
from app.brain.utilities import all_data_to_dict, user_data_to_dict, list_history_objs_to_dicts
from app.constants import TAXONOMY_CONSTANTS, HISTORY_CONSTNATS
from app.main import main_blueprint as main


@main.route('/')
def ts():
    serve_path = dirname(main.root_path)
    serve_path = join(serve_path, 'static')
    serve_path = join(serve_path, 'dist')
    serve_path = join(serve_path, 'index.html')
    return send_file(serve_path), 200


@main.route('/all-data')
def all_data():
    return dumps(all_data_to_dict(AllData.get_all_data())), 200


@main.route('/status')
def status():
    return dumps({'status': 'good'}), 200


@main.route('/user-data')
def user_data():
    if not current_user.is_authenticated:
        return dumps({'status': 'bad'}), 400
    return dumps(user_data_to_dict(UserData.get_user_data())), 200


@main.route('/history-by-taxonomy', methods=['POST'])
def history_by_taxonomy():
    if not current_user.is_authenticated:
        return dumps({'status': 'bad'}), 400

    history = RepExercisesManagement.get_user_history_by_exercise_id(
        user_id=current_user.id,
        exercise_id=request.args.get('exercise_id')
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

    RepExercisesManagement.submit_history_entry(
        user_id=current_user.id,
        exercise_id=request.args.get(HISTORY_CONSTNATS.EXERCISE_ID),
        sets=request.args.get(HISTORY_CONSTNATS.SETS),
        reps=request.args.get(HISTORY_CONSTNATS.REPS),
        weight=request.args.get(HISTORY_CONSTNATS.WEIGHT),
        exercise_date=request.args.get(HISTORY_CONSTNATS.DATE)
    )
    return dumps({'status': 'good'}), 200


@main.route('/get-valid-id-exercise-pairs', methods=['POST'])
def get_valid_id_exercise_pairs():
    return dumps({
        'pairs': RepExercisesManagement.get_valid_id_exercise_pairs()
    }), 200


@main.route('/add-rep-taxonomy', methods=['POST'])
def add_rep_taxonomy():
    if not request.args.get(TAXONOMY_CONSTANTS.NAME):  # This is the only required field
        return dumps({'status': 'bad'}), 400

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
    return dumps({'status': 'good'}), 200


@main.route('/login', methods=['POST'])
def login():
    parameters = request.get_json()
    email = parameters.get('email')
    password = parameters.get('password')
    login_result = Loginerator.login(email, password)
    if login_result == LoginResult.LOGGED_IN:
        return dumps({
            'status': 'good',
            'user_logged_in': current_user.nickname
        }), 200
    else:
        return dumps({'status': 'bad'}), 400


@main.route('/who-am-i', methods=['POST'])
def who_am_i():
    if current_user.is_authenticated:
        return dumps({
            'user': current_user.nickname
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
    email = request.args.get('email')
    nickname = request.args.get('nickname')
    password = request.args.get('password')
    reg_result = RegisterCity.register(email, nickname, password)
    if reg_result == RegisterResult.REGISTERED:
        return dumps({'status': 'good'}), 200
    else:
        return dumps({'status': 'bad'}), 400

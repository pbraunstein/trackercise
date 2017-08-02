from json import dumps

from flask import request
from flask_login import current_user


from app import csrf
from app.brain.exercises_management.rep_exercises_management import RepExercisesManagement
from app.brain.utilities import list_history_objs_to_dicts
from app.constants import TAXONOMY_CONSTANTS, HISTORY_CONSTANTS
from app.main import main_blueprint as main


@main.route('/rep-history-by-taxonomy', methods=['POST'])
def rep_history_by_taxonomy():
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


@main.route('/rep-history-by-date', methods=['POST'])
def rep_history_by_date():
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


@main.route('/get-valid-rep-id-exercise-pairs', methods=['POST'])
def get_valid_rep_id_exercise_pairs():
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

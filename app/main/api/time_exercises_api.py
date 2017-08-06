from json import dumps

from flask import request
from flask_login import current_user

from app import csrf
from app.brain.exercises_management.time_exercises_management import TimeExercisesManagement
from app.brain.utilities import list_history_objs_to_dicts
from app.constants import TAXONOMY_CONSTANTS, HISTORY_CONSTANTS
from app.main import main_blueprint as main


@main.route('/time-history-by-taxonomy', methods=['POST'])
def time_history_by_taxonomy():
    csrf.protect()

    if not current_user.is_authenticated:
        return dumps({'status': 'bad'}), 400

    parameters = request.get_json()

    history = TimeExercisesManagement.get_user_history_by_exercise_id(
        user_id=current_user.id,
        exercise_id=parameters.get('exercise_id')
    )

    return dumps({
        'status': 'good',
        'nickname': current_user.nickname,
        'history': list_history_objs_to_dicts(history)
    }), 200


@main.route('/time-history-by-date', methods=['POST'])
def time_history_by_date():
    csrf.protect()

    if not current_user.is_authenticated:
        return dumps({'status': 'bad'}), 400

    parameters = request.get_json()

    history = TimeExercisesManagement.get_user_history_by_date(
        user_id=current_user.id,
        exercise_date=parameters.get('exercise_date')
    )

    return dumps({
        'status': 'good',
        'nickname': current_user.nickname,
        'history': list_history_objs_to_dicts(history)
    }), 200


@main.route('/add-time-taxonomy', methods=['POST'])
def add_time_taxonomy():
    parameters = request.get_json()

    if not parameters.get(TAXONOMY_CONSTANTS.NAME):  # This is the only required field
        return dumps({'status': 'bad'}), 400

    TimeExercisesManagement.submit_taxonomy_entry(parameters.get(TAXONOMY_CONSTANTS.NAME))

    return dumps({'status': 'good'}), 200


@main.route('/add-time-history', methods=['POST'])
def add_time_history():
    if not current_user.is_authenticated:
        return dumps({'status': 'bad'}), 400

    parameters = request.get_json()

    TimeExercisesManagement.submit_history_entry(
        user_id=current_user.id,
        exercise_id=parameters.get(HISTORY_CONSTANTS.EXERCISE_ID),
        distance=parameters.get(HISTORY_CONSTANTS.DISTANCE),
        duration=parameters.get(HISTORY_CONSTANTS.DURATION),
        exercise_date=parameters.get(HISTORY_CONSTANTS.DATE)
    )

    return dumps({'status': 'good'}), 200

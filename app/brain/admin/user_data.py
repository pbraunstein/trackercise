from flask_login import current_user

from app.brain.utilities import prepare_history_entry
from service import RepExercisesHistoryService, RepExercisesTaxonomyService


class UserData(object):
    """
    Returns the relevant data for one user

    I N T E R F A C E   G U A R A N T E E D
    ---------------------------------------
    get_user_data(cls):
        -- Returns a dictionary with the nickname, user_id, all rep exercises history and rep exercises taxonomy
            specific to that user
    """
    @classmethod
    def get_user_data(cls):
        user_data = {'nickname': cls._get_current_user_nickname(), 'user_id': cls._get_current_user_id(),
                     'rep_history': cls._get_user_rep_history()}
        user_data['rep_taxonomies'] = cls._get_taxonomies_for_exercises(
            cls._convert_rep_exercises_to_exercise_ids(user_data['rep_history'])
        )
        return user_data

    @classmethod
    def _get_user_rep_history(cls):
        exercises = RepExercisesHistoryService.get_list_of_users_exercises(cls._get_current_user_id())
        return [prepare_history_entry(x) for x in exercises]

    @staticmethod
    def _get_current_user_nickname():
        return current_user.nickname

    @staticmethod
    def _get_current_user_id():
        return current_user.id

    @staticmethod
    def _convert_rep_exercises_to_exercise_ids(rep_exercises):
        return [x.exercise_id for x in rep_exercises]

    @staticmethod
    def _get_taxonomies_for_exercises(exercise_ids):
        return RepExercisesTaxonomyService.get_list_of_taxonomies_by_exercise_ids(exercise_ids)

# get user name
# get user's exercises

from flask_login import current_user

from brain.utilities import prepare_history_entry
from service import RepExercisesHistoryService


class UserData(object):
    @classmethod
    def get_user_data(cls):
        return {
            'nickname': cls._get_current_user_nickname(),
            'user_id': cls._get_current_user_id(),
            'rep_history': cls._get_user_rep_history()
        }

    @classmethod
    def _get_user_rep_history(cls):
        exercises = RepExercisesHistoryService.get_users_exercises(cls._get_current_user_id())
        return [prepare_history_entry(x) for x in exercises]

    @staticmethod
    def _get_current_user_nickname():
        return current_user.nickname

    @staticmethod
    def _get_current_user_id():
        return current_user.id


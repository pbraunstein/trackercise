# get user name
# get user's exercises

from flask_login import current_user


class UserData(object):
    @classmethod
    def get_user_data(cls):
        return {
            'nickname': cls._get_current_user_nickname(),
            'rep_history': cls._get_user_rep_history()
        }

    @staticmethod
    def _get_current_user_nickname():
        return current_user.nickname

    @staticmethod
    def _get_user_rep_history():
        pass

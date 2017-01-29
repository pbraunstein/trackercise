# get user name
# get user's exercises
# get user's taxonomies (set of exercise ids maybe?)

from flask_login import current_user


class UserData(object):
    @classmethod
    def get_user_data(cls):
        pass

    @staticmethod
    def get_current_user():
        return current_user.nickname

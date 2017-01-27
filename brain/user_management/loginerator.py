from flask_login import login_user, logout_user

from app import db
from login_result import LoginResult
from models import Users
from brain.utilities import hash_password


class Loginerator(object):
    """
    Manages the logic of logging in.

    I N T E R F A C E   G U A R A N T E E D
    ---------------------------------------
    login(email, password):
        -- Logs in a user if user exists and password is correct
        -- Returns a LoginResult describing what happened

    logout():
        -- Logs out the user if there is one logged in; otherwise does nothing
    """

    @classmethod
    def login(cls, email, password):
        user = cls._get_user_with_email(email)
        inputted_password_hash = hash_password(password)
        if user is None:
            return LoginResult.NO_SUCH_USER
        elif inputted_password_hash != user.password:
            return LoginResult.INCORRECT_PASSWORD
        else:  # credentials are a match
            login_user(user)
            return LoginResult.LOGGED_IN

    @staticmethod
    def logout():
        logout_user()

    @staticmethod
    def _get_user_with_email(email):
        return db.session.query(Users).filter(Users.email == email).first()
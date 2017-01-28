# from app import db
# from models import Users
from register_result import RegisterResult
from brain.utilities import hash_password

from service import UsersService


class RegisterCity(object):
    """
    Manages the logic of registering

    I N T E R F A C E   G U A R A N T E E D
    ---------------------------------------
    register(email, nickname, password):
        -- Register a user if the email is valid and doesn't yet exist
        -- Returns a RegisterResult describing what happened
    """
    @classmethod
    def register(cls, email, nickname, password):
        if not cls._user_email_is_valid(email):
            return RegisterResult.INVALID_EMAIL
        elif UsersService.user_with_email_already_exists(email):
            return RegisterResult.EMAIL_ALREADY_EXISTS
        else:  # all clear to register
            hashed_password = hash_password(password)
            UsersService.add_user_to_database(email, nickname, hashed_password)
            return RegisterResult.REGISTERED

    @staticmethod
    def _user_email_is_valid(email):
        return '@' in email and '.' in email

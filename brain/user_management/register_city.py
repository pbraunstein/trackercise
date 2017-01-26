from app import db
from models import Users
from register_result import RegisterResult
from brain.utilities import hash_password


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
        elif cls._user_already_exists(email):
            return RegisterResult.EMAIL_ALREADY_EXISTS
        else:  # all clear to register
            cls._add_user_to_database(email, nickname, password)
            return RegisterResult.REGISTERED

    @staticmethod
    def _user_email_is_valid(email):
        return '@' in email and '.' in email

    @staticmethod
    def _user_already_exists(email):
        users = Users.query.all()
        user_emails = [x.email for x in users]
        if email in user_emails:
            return True
        else:
            return False

    @staticmethod
    def _add_user_to_database(email, nickname, plain_text_password):
        """Owns hashing password"""
        hashed_password = hash_password(plain_text_password)
        new_user = Users(email=email, nickname=nickname, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

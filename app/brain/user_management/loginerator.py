from flask_login import login_user, logout_user, current_user

from app.brain.user_management.login_result import LoginResult
from app.brain.utilities import hash_password
from app.service import UsersService


class Loginerator(object):
    """
    Manages the logic of logging in.

    I N T E R F A C E   G U A R A N T E E D
    ---------------------------------------
    login(email, password):
        -- Logs in a user if user exists and password is correct
        -- If credentials match, marks the user as authenticated in the Users table
        -- Returns a LoginResult describing what happened

    logout():
        -- Logs out the user if there is one logged in; otherwise does nothing
        -- Marks the former current_users as not authenticated in the Users table
    """

    @staticmethod
    def login(email, password):
        user = UsersService.get_user_with_email(email)
        inputted_password_hash = hash_password(password)
        if user is None:
            return LoginResult.NO_SUCH_USER
        elif inputted_password_hash != user.password:
            return LoginResult.INCORRECT_PASSWORD
        else:  # credentials are a match
            login_user(user)
            UsersService.mark_user_as_authenticated(user)
            return LoginResult.LOGGED_IN

    @staticmethod
    def logout():
        if not current_user.is_authenticated:
            return
        UsersService.mark_user_as_not_authenticated(
            UsersService.get_user_with_email(
                current_user.email
            )
        )
        logout_user()

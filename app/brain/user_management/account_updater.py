from flask_login import current_user

from app.brain.user_management.change_password_result import ChangePasswordResult
from app.brain.utilities import hash_password
from app.service import UsersService


class AccountUpdater(object):
    @staticmethod
    def change_password(old_password, new_password, confirm_password):
        if new_password != confirm_password:
            return ChangePasswordResult.NEW_PASSWORDS_DO_NOT_MATCH
        elif not current_user.is_authenticated:
            # Some how the user isn't logged in --- this should never happen
            return ChangePasswordResult.CURRENT_PASSWORD_INCORRECT
        elif hash_password(old_password) != current_user.password:
            return ChangePasswordResult.CURRENT_PASSWORD_INCORRECT
        else:
            # If we get to here, we go ahead and change the password
            UsersService.change_password(current_user, hash_password(new_password))

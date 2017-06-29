import unittest

from mock import patch, PropertyMock

from app.brain.user_management.account_updater import AccountUpdater
from app.brain.user_management.change_password_result import ChangePasswordResult


class AccountUpdateTests(unittest.TestCase):
    @patch('app.brain.user_management.account_updater.UsersService.change_password')
    def test_change_password_mismatched_new_confirm(self, change_password_mock):
        result = AccountUpdater.change_password('old_password', 'new_password', 'does_not_match')
        self.assertEqual(result, ChangePasswordResult.NEW_PASSWORDS_DO_NOT_MATCH)

    @patch('app.brain.user_management.account_updater.current_user')
    @patch('app.brain.user_management.account_updater.UsersService.change_password')
    def test_change_password_user_not_authenticated(self, change_password_mock, current_user_mock):
        type(current_user_mock.return_value).is_authenticated = True
        result = AccountUpdater.change_password('old_password', 'new_password', 'new_password')
        self.assertEqual(result, ChangePasswordResult.CURRENT_PASSWORD_INCORRECT)

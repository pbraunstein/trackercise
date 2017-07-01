import unittest

from mock import patch

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
        type(current_user_mock.return_value).is_authenticated = False
        result = AccountUpdater.change_password('old_password', 'new_password', 'new_password')
        self.assertEqual(result, ChangePasswordResult.CURRENT_PASSWORD_INCORRECT)

    @patch('app.brain.user_management.account_updater.hash_password')
    @patch('app.brain.user_management.account_updater.current_user')
    @patch('app.brain.user_management.account_updater.UsersService.change_password')
    def test_change_password_old_password_does_not_match(self, change_password_mock, current_user_mock, hash_mock):
        hash_mock.return_value = 'password_1'
        current_user_mock.is_authenticated = True
        current_user_mock.password = 'password_2'

        result = AccountUpdater.change_password('old_password', 'new_password', 'new_password')
        self.assertEqual(result, ChangePasswordResult.CURRENT_PASSWORD_INCORRECT)

    @patch('app.brain.user_management.account_updater.hash_password')
    @patch('app.brain.user_management.account_updater.current_user')
    @patch('app.brain.user_management.account_updater.UsersService.change_password')
    def test_change_password_successful_change(self, change_password_mock, current_user_mock, hash_mock):
        hash_mock.return_value = 'password_1'
        current_user_mock.is_authenticated = True
        current_user_mock.password = 'password_1'

        result = AccountUpdater.change_password('old_password', 'new_password', 'new_password')
        self.assertEqual(result, ChangePasswordResult.PASSWORD_CHANGE_SUCCESSFUL)

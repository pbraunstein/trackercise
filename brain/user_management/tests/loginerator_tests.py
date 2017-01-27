import unittest

from mock import patch, PropertyMock

import app  # otherwise broken by circular imports :(
from brain.user_management.loginerator import Loginerator
from brain.user_management.login_result import LoginResult


class LogineratorTests(unittest.TestCase):
    @patch('brain.utilities.hash_password')
    @patch.object(Loginerator, '_get_user_with_email')
    def test_login_no_user(self, get_user_mock, hash_mock):
        get_user_mock.return_value = None
        result = Loginerator.login('test@test.test', 'super_secret_password')
        self.assertEqual(result, LoginResult.NO_SUCH_USER)

    @patch('brain.user_management.loginerator.hash_password')
    @patch.object(Loginerator, '_get_user_with_email')
    def test_login_incorrect_password(self, get_user_mock, hash_mock):
        hash_mock.return_value = 'not_secret_password'
        result = Loginerator.login('test@test.test', 'super_secret_password')
        self.assertEqual(result, LoginResult.INCORRECT_PASSWORD)

    @patch('brain.user_management.loginerator.login_user')
    @patch('brain.user_management.loginerator.hash_password')
    @patch.object(Loginerator, '_get_user_with_email')
    def test_login_success(self, get_user_mock, hash_mock, login_mock):
        hash_mock.return_value = 'abcdef1234'
        type(get_user_mock.return_value).password = PropertyMock(return_value='abcdef1234')
        result = Loginerator.login('test@test.test', 'super_secret_password')
        self.assertEqual(result, LoginResult.LOGGED_IN)
import unittest

from mock import patch, PropertyMock

from app.brain.user_management.login_result import LoginResult
from app.brain.user_management.loginerator import Loginerator


class LogineratorTests(unittest.TestCase):
    # login tests #
    @patch('app.brain.utilities.hash_password')
    @patch('app.brain.user_management.loginerator.UsersService.get_user_with_email')
    def test_login_no_user(self, get_user_mock, hash_mock):
        get_user_mock.return_value = None
        result = Loginerator.login('test@test.test', 'super_secret_password')
        self.assertEqual(result, LoginResult.NO_SUCH_USER)

    @patch('app.brain.user_management.loginerator.hash_password')
    @patch('app.brain.user_management.loginerator.UsersService.get_user_with_email')
    def test_login_incorrect_password(self, get_user_mock, hash_mock):
        hash_mock.return_value = 'not_secret_password'
        result = Loginerator.login('test@test.test', 'super_secret_password')
        self.assertEqual(result, LoginResult.INCORRECT_PASSWORD)

    @patch('app.brain.user_management.loginerator.login_user')
    @patch('app.brain.user_management.loginerator.hash_password')
    @patch('app.brain.user_management.loginerator.UsersService.get_user_with_email')
    @patch('app.brain.user_management.loginerator.UsersService.mark_user_as_authenticated')
    def test_login_success(self, authentication_mock, get_user_mock, hash_mock, login_mock):
        hash_mock.return_value = 'abcdef1234'
        type(get_user_mock.return_value).password = PropertyMock(return_value='abcdef1234')
        result = Loginerator.login('test@test.test', 'super_secret_password')
        self.assertEqual(result, LoginResult.LOGGED_IN)

    # logout tests #
    @patch('app.brain.user_management.loginerator.current_user')
    @patch('app.brain.user_management.loginerator.UsersService.mark_user_as_not_authenticated')
    def test_logout_no_user_logged_in(self, deauthentication_mock, current_user_mock):
        type(current_user_mock).is_authenticated = PropertyMock(return_value=False)
        Loginerator.logout()
        self.assertFalse(deauthentication_mock.called)

    @patch('app.brain.user_management.loginerator.logout_user')
    @patch('app.brain.user_management.loginerator.current_user')
    @patch('app.brain.user_management.loginerator.UsersService.mark_user_as_not_authenticated')
    @patch('app.brain.user_management.loginerator.UsersService.get_user_with_email')
    def test_logout_with_user_logged_in(self, get_user_mock, deauthentication_mock, current_user_mock, logout_mock):
        type(current_user_mock).is_authenticated = PropertyMock(return_value=True)
        Loginerator.logout()
        self.assertTrue(deauthentication_mock.called)

import unittest

from mock import patch

from app.brain.user_management.register_result import RegisterResult
from app.brain.user_management.register_city import RegisterCity



class RegisterCityTests(unittest.TestCase):
    # register tests
    @patch.object(RegisterCity, '_user_email_is_valid')
    def test_register_invalid_email(self, validator_mock):
        validator_mock.return_value = False
        result = RegisterCity.register('test@test.test', 'test_man', 'password')
        self.assertEqual(result, RegisterResult.INVALID_EMAIL)

    @patch('brain.user_management.loginerator.UsersService.user_with_email_already_exists')
    @patch.object(RegisterCity, '_user_email_is_valid')
    def test_register_duplicate_email(self, validator_mock, exists_mock):
        validator_mock.return_value = True
        exists_mock.return_value = True
        result = RegisterCity.register('test@test.test', 'test_man', 'password')
        self.assertEqual(result, RegisterResult.EMAIL_ALREADY_EXISTS)

    @patch('brain.user_management.loginerator.UsersService.add_user_to_database')
    @patch('brain.user_management.loginerator.UsersService.user_with_email_already_exists')
    @patch.object(RegisterCity, '_user_email_is_valid')
    def test_register_successful_registration(self, validator_mock, exists_mock, add_to_db_mock):
        validator_mock.return_value = True
        exists_mock.return_value = False
        result = RegisterCity.register('test@test.test', 'test_man', 'password')
        self.assertEqual(result, RegisterResult.REGISTERED)

    # _user_email_is_valid_tests
    def test_user_email_is_valid_no_at(self):
        is_valid = RegisterCity._user_email_is_valid('hi.')
        self.assertFalse(is_valid)

    def test_user_email_is_valid_no_dot(self):
        is_valid = RegisterCity._user_email_is_valid('hi@')
        self.assertFalse(is_valid)

    def test_user_email_is_valid_valid_email(self):
        is_valid = RegisterCity._user_email_is_valid('hi@.')
        self.assertTrue(is_valid)

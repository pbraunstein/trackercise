import unittest

from mock import patch

import app  # otherwise broken by circular imports :(
from brain.user_management.register_city import RegisterCity
from brain.user_management.register_result import RegisterResult


class RegisterCityTests(unittest.TestCase):
    @patch.object(RegisterCity, '_user_email_is_valid')
    def test_register_invalid_email(self, validator_mock):
        validator_mock.return_value = False
        result = RegisterCity.register('test@test.test', 'test_man', 'password')
        self.assertEqual(result, RegisterResult.INVALID_EMAIL)

    @patch.object(RegisterCity, '_user_already_exists')
    @patch.object(RegisterCity, '_user_email_is_valid')
    def test_register_duplicate_email(self, validator_mock, exists_mock):
        validator_mock.return_value = True
        exists_mock.return_value = True
        result = RegisterCity.register('test@test.test', 'test_man', 'password')
        self.assertEqual(result, RegisterResult.EMAIL_ALREADY_EXISTS)

    @patch.object(RegisterCity, '_add_user_to_database')
    @patch.object(RegisterCity, '_user_already_exists')
    @patch.object(RegisterCity, '_user_email_is_valid')
    def test_register_successful_registration(self, validator_mock, exists_mock, add_to_db_mock):
        validator_mock.return_value = True
        exists_mock.return_value = False
        result = RegisterCity.register('test@test.test', 'test_man', 'password')
        self.assertEqual(result, RegisterResult.REGISTERED)

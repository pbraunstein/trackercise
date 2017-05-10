import unittest

from mock import patch

from app.brain.admin.all_data import AllData
from app.constants import USERS_CONSTANTS, TAXONOMY_CONSTANTS, HISTORY_CONSTNATS


class AllDataTests(unittest.TestCase):

    @patch('app.service.RepExercisesHistoryService.get_list_of_all_history')
    @patch('app.service.RepExercisesTaxonomyService.get_list_of_all_exercises')
    @patch('app.service.UsersService.get_list_of_all_users')
    def test_empty_return_values(self, users_mock, taxonomy_mock, history_mock):
        users_mock.return_value = []
        taxonomy_mock.return_value = []
        history_mock.return_value = []

        result = AllData.get_all_data()
        expected_result = {
            USERS_CONSTANTS.NAME: [],
            TAXONOMY_CONSTANTS.GROUP_NAME: [],
            HISTORY_CONSTNATS.NAME: []
        }

        self.assertEqual(result, expected_result)

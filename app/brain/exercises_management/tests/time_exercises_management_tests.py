import unittest
from datetime import date

from mock import patch

from app.brain.exercises_management.time_exercises_management import TimeExercisesManagement
from app.models import TimeExercisesTaxonomy, TimeExercisesHistory


class TimeExercisesManagementTests(unittest.TestCase):
    @patch(
        'app.brain.exercises_management.time_exercises_management.TimeExercisesTaxonomyService'
        '.get_list_of_all_exercises'
    )
    def test_get_valid_id_exercise_pairs(self, taxonomy_service_mock):
        exercises = [
            TimeExercisesTaxonomy(name='c_exercise'),
            TimeExercisesTaxonomy(name='a_exercise'),
            TimeExercisesTaxonomy(name='e_exercise'),
            TimeExercisesTaxonomy(name='d_exercise'),
            TimeExercisesTaxonomy(name='b_exercise')
        ]
        exercises[0].id = 1
        exercises[1].id = 2
        exercises[2].id = 3
        exercises[3].id = 4
        exercises[4].id = 5
        taxonomy_service_mock.return_value = exercises
        expected_results = [
            ('2', 'a_exercise'),
            ('5', 'b_exercise'),
            ('1', 'c_exercise'),
            ('4', 'd_exercise'),
            ('3', 'e_exercise'),
        ]
        actual_results = TimeExercisesManagement.get_valid_id_exercise_pairs()
        self.assertListEqual(actual_results, expected_results)

    @patch(
        'app.brain.exercises_management.time_exercises_management.TimeExercisesHistoryService'
        '.get_user_history_by_exercise'
    )
    def test_get_user_history_by_exercise_id(self, taxonomy_service_mock):
        history_1 = TimeExercisesHistory(
            user_id=1,
            exercise_id=1,
            distance=2.2,
            duration=28,
            exercise_date=date(year=2017, month=8, day=2)
        )
        history_2 = TimeExercisesHistory(
            user_id=1,
            exercise_id=1,
            distance=2.3,
            duration=31,
            exercise_date=date(year=2017, month=9, day=2)
        )

        history_3 = TimeExercisesHistory(
            user_id=1,
            exercise_id=1,
            distance=2.0,
            duration=27,
            exercise_date=date(year=2017, month=7, day=2)
        )
        history_4 = TimeExercisesHistory(
            user_id=1,
            exercise_id=1,
            distance=2.2,
            duration=28,
            exercise_date=date(year=2017, month=1, day=21)
        )
        history_5 = TimeExercisesHistory(
            user_id=1,
            exercise_id=1,
            distance=3.0,
            duration=30,
            exercise_date=date(year=2017, month=7, day=21)
        )

        history = [
            history_1,
            history_2,
            history_3,
            history_4,
            history_5
        ]

        history_sorted = [
            history_4,
            history_3,
            history_5,
            history_1,
            history_2
        ]
        taxonomy_service_mock.return_value = history
        user_id = 1
        exercise_id = 1

        actual_results = TimeExercisesManagement.get_user_history_by_exercise_id(user_id, exercise_id)
        expected_results = history_sorted

        # make sure contents and order the same
        self.assertListEqual(actual_results, expected_results)

        # make sure contents are in ascending date order
        self.assertListEqual(actual_results, sorted(actual_results, key=lambda x: x.exercise_date))

        # make sure the service method was called
        taxonomy_service_mock.assert_called_once_with(user_id, exercise_id)

    @patch(
        'app.brain.exercises_management.time_exercises_management.TimeExercisesHistoryService'
        '.get_user_history_by_exercise'
    )
    def test_get_user_history_by_exercise_id_no_matches(self, taxonomy_service_mock):
        taxonomy_service_mock.return_value = []
        user_id = 1
        exercise_id = 2

        actual_results = TimeExercisesManagement.get_user_history_by_exercise_id(user_id, exercise_id)
        expected_results = []

        self.assertListEqual(actual_results, expected_results)

        # make sure the service method was called
        taxonomy_service_mock.assert_called_once_with(user_id, exercise_id)

    @patch('app.brain.exercises_management.time_exercises_management.TimeExercisesHistoryService.add_entry_to_db')
    def test_submit_history_entry(self, db_mock):
        expected_date = date(year=1999, month=11, day=30)
        expected_result = TimeExercisesHistory(
            user_id=3,
            exercise_id=14,
            distance=23.2,
            duration=24,
            exercise_date=expected_date
        )

        actual_result = TimeExercisesManagement.submit_history_entry(
            user_id=3,
            exercise_id=14,
            distance=23.2,
            duration=24,
            exercise_date=expected_date
        )

        self.assertEqual(actual_result, expected_result)

        # make sure the service method was called
        db_mock.assert_called_once_with(actual_result)

    @patch('app.brain.exercises_management.time_exercises_management.TimeExercisesTaxonomyService.add_entry_to_db')
    def test_submit_taxonomy_entry(self, db_mock):
        exercise_name = 'rowing'
        expected_entry = TimeExercisesTaxonomy(name=exercise_name)
        actual_entry = TimeExercisesManagement.submit_taxonomy_entry('rowing')

        self.assertEqual(actual_entry, expected_entry)

        # make sure mock was called
        db_mock.assert_called_once_with(actual_entry)

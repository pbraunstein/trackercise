import unittest
from datetime import date

from mock import patch

from app.brain.exercises_management.time_exercises_management import TimeExercisesManagement
from app.models import TimeExercisesTaxonomy, TimeExercisesHistory


class TimeExercisesManagementTests(unittest.TestCase):
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

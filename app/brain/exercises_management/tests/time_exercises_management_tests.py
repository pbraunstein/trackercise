import unittest

from mock import patch

from app.brain.exercises_management.time_exercises_management import TimeExercisesManagement
from app.models import TimeExercisesTaxonomy


class TimeExercisesManagementTests(unittest.TestCase):
    @patch('app.brain.exercises_management.time_exercises_management.TimeExercisesTaxonomyService.add_entry_to_db')
    def test_submit_taxonomy_entry(self, db_mock):
        exercise_name = 'rowing'
        expected_entry = TimeExercisesTaxonomy(name=exercise_name)
        actual_entry = TimeExercisesManagement.submit_taxonomy_entry('rowing')

        self.assertEqual(actual_entry, expected_entry)

        # make sure mock was called
        db_mock.assert_called_once_with(actual_entry)

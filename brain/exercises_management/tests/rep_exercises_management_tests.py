from mock import patch
import unittest

import app
from brain.exercises_management.rep_exercises_management import RepExercisesManagement
from models import RepExercisesTaxonomy


class RepExercisesManagementTests(unittest.TestCase):
    def setUp(self):
        self.exercises = [
            RepExercisesTaxonomy(
                name='exercise_1',
                is_back=True,
                is_chest=True,
                is_shoulders=False,
                is_biceps=True,
                is_triceps=True,
                is_legs=False,
                is_core=False,
                is_balance=False,
                is_cardio=False,
                is_weight_per_hand=True
            ),
            RepExercisesTaxonomy(
                name='exercise_2',
                is_back=True,
                is_chest=True,
                is_shoulders=True,
                is_biceps=True,
                is_triceps=True,
                is_legs=False,
                is_core=False,
                is_balance=False,
                is_cardio=False,
                is_weight_per_hand=True
            ),
            RepExercisesTaxonomy(
                name='exercise_3',
                is_back=True,
                is_chest=True,
                is_shoulders=False,
                is_biceps=True,
                is_triceps=True,
                is_legs=False,
                is_core=True,
                is_balance=False,
                is_cardio=False,
                is_weight_per_hand=True
            )
        ]
        self.exercises[0].id = 1
        self.exercises[1].id = 2
        self.exercises[2].id = 3

    @patch('brain.exercises_management.rep_exercises_management.RepExercisesTaxonomyService.get_list_of_all_exercises')
    def test_get_valid_id_exercise_pairs(self, taxonomy_service_mock):
        taxonomy_service_mock.return_value = self.exercises
        expected_results = [('1', 'exercise_1'), ('2', 'exercise_2'), ('3', 'exercise_3')]
        actual_results = RepExercisesManagement.get_valid_id_exercise_pairs()
        self.assertListEqual(actual_results, expected_results)

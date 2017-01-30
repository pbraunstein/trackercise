from datetime import date
from mock import patch
import unittest

import app
from brain.exercises_management.rep_exercises_management import RepExercisesManagement
from models import RepExercisesTaxonomy, RepExercisesHistory


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

    @patch('brain.exercises_management.rep_exercises_management.RepExercisesHistoryService.add_entry_to_db')
    def test_submit_history_entry(self, db_mock):
        expected_result = RepExercisesHistory(
            user_id=3,
            exercise_id=12,
            sets=3,
            reps=12,
            weight=12.5,
            date=date.today()
        )
        actual_result = RepExercisesManagement.submit_history_entry(user_id=3,
                                                                    exercise_id=12,
                                                                    sets=3,
                                                                    reps=12,
                                                                    weight=12.5,
                                                                    )
        self.assertEqual(actual_result.user_id, expected_result.user_id)
        self.assertEqual(actual_result.exercise_id, expected_result.exercise_id)
        self.assertEqual(actual_result.sets, expected_result.sets)
        self.assertEqual(actual_result.reps, expected_result.reps)
        self.assertEqual(actual_result.weight, expected_result.weight)
        self.assertEqual(actual_result.date, expected_result.date)


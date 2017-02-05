import unittest
from datetime import date

from mock import patch

from app.brain.exercises_management.rep_exercises_management import RepExercisesManagement
from app.models import RepExercisesTaxonomy, RepExercisesHistory


class RepExercisesManagementTests(unittest.TestCase):
    def setUp(self):
        self.exercises = [
            RepExercisesTaxonomy(
                name='c_exercise',
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
                name='e_exercise',
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
                name='b_exercise',
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
            ),
            RepExercisesTaxonomy(
                name='a_exercise',
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
                name='d_exercise',
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
        self.exercises[3].id = 4
        self.exercises[4].id = 5

    @patch(
        'app.brain.exercises_management.rep_exercises_management.RepExercisesTaxonomyService.get_list_of_all_exercises')
    def test_get_valid_id_exercise_pairs(self, taxonomy_service_mock):
        taxonomy_service_mock.return_value = self.exercises
        expected_results = [('4', 'a_exercise'), ('3', 'b_exercise'), ('1', 'c_exercise'), ('5', 'd_exercise'),
                            ('2', 'e_exercise')]
        actual_results = RepExercisesManagement.get_valid_id_exercise_pairs()
        self.assertListEqual(actual_results, expected_results)

    @patch(
        'app.brain.exercises_management.rep_exercises_management.RepExercisesHistoryService'
        '.get_user_history_by_exercise'
    )
    def test_get_user_history_by_exercise_id(self, db_mock):
        pass

    @patch('app.brain.exercises_management.rep_exercises_management.RepExercisesHistoryService.add_entry_to_db')
    def test_submit_history_entry(self, db_mock):
        expected_date = date(year=2000, month=12, day=23)
        expected_result = RepExercisesHistory(
            user_id=3,
            exercise_id=12,
            sets=3,
            reps=12,
            weight=12.5,
            date=expected_date
        )
        actual_result = RepExercisesManagement.submit_history_entry(user_id=3,
                                                                    exercise_id=12,
                                                                    sets=3,
                                                                    reps=12,
                                                                    weight=12.5,
                                                                    exercise_date=expected_date
                                                                    )
        # make sure results are the same
        self.assertEqual(actual_result.user_id, expected_result.user_id)
        self.assertEqual(actual_result.exercise_id, expected_result.exercise_id)
        self.assertEqual(actual_result.sets, expected_result.sets)
        self.assertEqual(actual_result.reps, expected_result.reps)
        self.assertEqual(actual_result.weight, expected_result.weight)
        self.assertEqual(actual_result.date, expected_result.date)

        # make sure the service method was called
        db_mock.assert_called_once_with(actual_result)

    @patch('app.brain.exercises_management.rep_exercises_management.RepExercisesTaxonomyService.add_entry_to_db')
    def test_submit_taxonomy_entry(self, db_mock):
        exercise_name = 'super_awesome_exercise'
        expected_entry = RepExercisesTaxonomy(
            name=exercise_name,
            is_back=True,
            is_chest=False,
            is_shoulders=False,
            is_biceps=True,
            is_triceps=True,
            is_legs=False,
            is_core=False,
            is_balance=True,
            is_cardio=True,
            is_weight_per_hand=True
        )

        actual_entry = RepExercisesManagement.submit_taxonomy_entry(
            name=exercise_name,
            is_back=True,
            is_chest=False,
            is_shoulders=False,
            is_biceps=True,
            is_triceps=True,
            is_legs=False,
            is_core=False,
            is_balance=True,
            is_cardio=True,
            is_weight_per_hand=True
        )

        # make sure results are the same
        self.assertEqual(actual_entry.name, expected_entry.name)
        self.assertEqual(actual_entry.is_back, expected_entry.is_back)
        self.assertEqual(actual_entry.is_chest, expected_entry.is_chest)
        self.assertEqual(actual_entry.is_shoulders, expected_entry.is_shoulders)
        self.assertEqual(actual_entry.is_biceps, expected_entry.is_biceps)
        self.assertEqual(actual_entry.is_triceps, expected_entry.is_triceps)
        self.assertEqual(actual_entry.is_legs, expected_entry.is_legs)
        self.assertEqual(actual_entry.is_core, expected_entry.is_core)
        self.assertEqual(actual_entry.is_balance, expected_entry.is_balance)
        self.assertEqual(actual_entry.is_cardio, expected_entry.is_cardio)
        self.assertEqual(actual_entry.is_weight_per_hand, expected_entry.is_weight_per_hand)

        # make sure the service method was called
        db_mock.assert_called_once_with(actual_entry)

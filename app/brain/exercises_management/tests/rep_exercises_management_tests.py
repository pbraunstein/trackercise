import unittest
from datetime import date

from mock import patch

from app.brain.custom_exceptions import ThisShouldNeverHappenException
from app.brain.exercises_management.rep_exercises_management import RepExercisesManagement
from app.models import RepExercisesTaxonomy, RepExercisesHistory


class RepExercisesManagementTests(unittest.TestCase):
    def setUp(self):
        history_1 = RepExercisesHistory(
            user_id=1,
            exercise_id=27,
            sets=2,
            reps=12,
            weight=45,
            date=date(year=2016, month=4, day=12)
        )
        history_2 = RepExercisesHistory(
            user_id=1,
            exercise_id=27,
            sets=2,
            reps=12,
            weight=45,
            date=date(year=2016, month=4, day=16)
        )
        history_3 = RepExercisesHistory(
            user_id=1,
            exercise_id=27,
            sets=2,
            reps=16,
            weight=40,
            date=date(year=2016, month=4, day=14)
        )
        self.history = [
            history_1,
            history_2,
            history_3
        ]

        self.history_sorted = [
            history_1,
            history_3,
            history_2
        ]

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
        db_mock.return_value = self.history
        user_id = 1
        exercise_id = 27
        expected_results = self.history_sorted
        actual_results = RepExercisesManagement.get_user_history_by_exercise_id(user_id, exercise_id)

        # make sure contents and order the same
        self.assertListEqual(actual_results, expected_results)

        # make sure contents are in ascending date order
        self.assertListEqual(actual_results, sorted(actual_results, key=lambda x: x.date))

        # make sure the service method was called
        db_mock.assert_called_once_with(user_id, exercise_id)

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

        self.assertEqual(actual_result, expected_result)

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
        self.assertEqual(actual_entry, expected_entry)

        # make sure the service method was called
        db_mock.assert_called_once_with(actual_entry)

    # convert_ts_strings_to_booleans test #
    def test_convert_ts_strings_to_booleans_false(self):
        self.assertFalse(RepExercisesManagement.convert_ts_strings_to_booleans('false'))

    def test_convert_ts_strings_to_booleans_true(self):
        self.assertTrue(RepExercisesManagement.convert_ts_strings_to_booleans('true'))

    def test_convert_ts_strings_to_booleans_invalid_input(self):
        with self.assertRaises(ThisShouldNeverHappenException):
            RepExercisesManagement.convert_ts_strings_to_booleans('True')

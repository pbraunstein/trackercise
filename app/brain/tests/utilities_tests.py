import unittest
from datetime import date

from app.brain.custom_exceptions import ThisShouldNeverHappenException
from app.brain.utilities import prepare_history_entry, _user_obj_to_dict, _taxonomy_obj_to_dict, _history_obj_to_dict
from app.constants import USERS_CONSTANTS, TAXONOMY_CONSTANTS, HISTORY_CONSTANTS
from app.models import Users, RepExercisesTaxonomy, RepExercisesHistory, TimeExercisesHistory, TimeExercisesTaxonomy


class UtilitiesTests(unittest.TestCase):
    # prepare_history_entry tests #
    def test_prepare_history_entry_stringifies_date(self):
        test_entry = RepExercisesHistory(
            user_id=1,
            exercise_id=12,
            sets=1,
            reps=10,
            weight=20,
            date=date.today()
        )
        test_entry = prepare_history_entry(test_entry)
        self.assertIsInstance(test_entry.date, str)

    # _user_obj_to_dict tests #
    def test_user_obj_to_dict(self):
        test_email = 'test@test.test'
        test_nickname = 'test_name'
        test_password = '1234'
        test_id = 1

        user_obj = Users(
            email=test_email,
            nickname=test_nickname,
            password=test_password
        )

        user_obj.id = test_id  # have to set this manually because there is no db

        result = _user_obj_to_dict(user_obj)
        expected_result = {
            USERS_CONSTANTS.ID: test_id,
            USERS_CONSTANTS.EMAIL: test_email,
            USERS_CONSTANTS.NICKNAME: test_nickname,
            USERS_CONSTANTS.PASSWORD: test_password,
            USERS_CONSTANTS.AUTHENTICATED: False
        }

        self.assertDictEqual(result, expected_result)

    # _taxonomy_obj_to_dict tests #
    def test_rep_taxonomy_obj_to_dict(self):
        test_id = 42
        test_name = 'squat'
        test_is_back = True
        test_is_chest = False
        test_is_shoulders = True
        test_is_biceps = False
        test_is_triceps = False
        test_is_legs = True
        test_is_core = True
        test_is_balance = True
        test_is_cardio = False
        test_is_weight_per_hand = False

        taxonomy_obj = RepExercisesTaxonomy(
            name=test_name,
            is_back=test_is_back,
            is_chest=test_is_chest,
            is_shoulders=test_is_shoulders,
            is_biceps=test_is_biceps,
            is_triceps=test_is_triceps,
            is_legs=test_is_legs,
            is_core=test_is_core,
            is_balance=test_is_balance,
            is_cardio=test_is_cardio,
            is_weight_per_hand=test_is_weight_per_hand
        )

        taxonomy_obj.id = test_id  # have to set this manually because there is no db

        actual_result = _taxonomy_obj_to_dict(taxonomy_obj)

        expected_result = {
            TAXONOMY_CONSTANTS.ID: test_id,
            TAXONOMY_CONSTANTS.NAME: test_name,
            TAXONOMY_CONSTANTS.IS_BACK: test_is_back,
            TAXONOMY_CONSTANTS.IS_CHEST: test_is_chest,
            TAXONOMY_CONSTANTS.IS_SHOULDERS: test_is_shoulders,
            TAXONOMY_CONSTANTS.IS_BICEPS: test_is_biceps,
            TAXONOMY_CONSTANTS.IS_TRICEPS: test_is_triceps,
            TAXONOMY_CONSTANTS.IS_LEGS: test_is_legs,
            TAXONOMY_CONSTANTS.IS_CORE: test_is_core,
            TAXONOMY_CONSTANTS.IS_BALANCE: test_is_balance,
            TAXONOMY_CONSTANTS.IS_CARDIO: test_is_cardio,
            TAXONOMY_CONSTANTS.IS_WEIGHT_PER_HAND: test_is_weight_per_hand
        }

        self.assertDictEqual(actual_result, expected_result)

    def test_time_taxonomy_obj_to_dict(self):
        test_id = 42
        test_name = 'running'

        taxonomy_obj = TimeExercisesTaxonomy(
            name=test_name
        )
        taxonomy_obj.id = test_id  # have to set this manually because there is no db

        actual_result = _taxonomy_obj_to_dict(taxonomy_obj)

        expected_result = {
            TAXONOMY_CONSTANTS.ID: test_id,
            TAXONOMY_CONSTANTS.NAME: test_name
        }

        self.assertDictEqual(actual_result, expected_result)

    def test_unknown_type_taxonomy_obj_to_dict(self):
        with self.assertRaises(ThisShouldNeverHappenException):
            _taxonomy_obj_to_dict(TimeExercisesHistory(
                user_id=1,
                exercise_id=2,
                distance=12,
                duration=68,
                exercise_date=date.today()
            ))

    # _history_obj_to_dict tests #
    def test_rep_history_obj_to_dict(self):
        test_id = 18
        test_user_id = 23
        test_exercise_id = 4
        test_sets = 5
        test_reps = 5
        test_weight = 20
        test_date = date.today()

        rep_history_obj = RepExercisesHistory(
            user_id=test_user_id,
            exercise_id=test_exercise_id,
            sets=test_sets,
            reps=test_reps,
            weight=test_weight,
            date=test_date
        )

        rep_history_obj.id = test_id  # have to set this manually because there is no db

        actual_results = _history_obj_to_dict(rep_history_obj)

        expected_results = {
            HISTORY_CONSTANTS.ID: test_id,
            HISTORY_CONSTANTS.USER_ID: test_user_id,
            HISTORY_CONSTANTS.EXERCISE_ID: test_exercise_id,
            HISTORY_CONSTANTS.SETS: test_sets,
            HISTORY_CONSTANTS.REPS: test_reps,
            HISTORY_CONSTANTS.WEIGHT: test_weight,
            HISTORY_CONSTANTS.DATE: str(test_date)
        }

        self.assertDictEqual(actual_results, expected_results)

    def test_time_history_obj_to_dict(self):
        test_id = 15
        test_user_id = 42
        test_exercise_id = 12
        test_distance = 14
        test_duration = 50
        test_exercise_date = date.today()

        time_history_obj = TimeExercisesHistory(
            user_id=test_user_id,
            exercise_id=test_exercise_id,
            distance=test_distance,
            duration=test_duration,
            exercise_date=test_exercise_date
        )

        time_history_obj.id = test_id  # have to set this manually because there is no db

        actual_results = _history_obj_to_dict(time_history_obj)

        expected_results = {
            HISTORY_CONSTANTS.ID: test_id,
            HISTORY_CONSTANTS.USER_ID: test_user_id,
            HISTORY_CONSTANTS.EXERCISE_ID: test_exercise_id,
            HISTORY_CONSTANTS.DISTANCE: test_distance,
            HISTORY_CONSTANTS.DURATION: test_duration,
            HISTORY_CONSTANTS.DATE: str(test_exercise_date)
        }

        self.assertDictEqual(actual_results, expected_results)

    def test_unknown_type_history_obj_to_dict(self):
        # Passing an object that is neither a RepExercisesTaxonomy nor a TimeExercisesTaxonomy
        # should result in a ThisShouldNeverHappen exception being raised
        with self.assertRaises(ThisShouldNeverHappenException):
            _history_obj_to_dict(RepExercisesTaxonomy(
                name='test_exercise',
                is_back=True,
                is_chest=False,
                is_shoulders=True,
                is_biceps=True,
                is_triceps=False,
                is_legs=False,
                is_core=True,
                is_balance=False,
                is_cardio=False,
                is_weight_per_hand=False
            ))



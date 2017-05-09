import unittest
from datetime import date

from app.brain.utilities import prepare_history_entry, _user_obj_to_dict, _taxonomy_obj_to_dict
from app.constants import USERS, TAXONOMY, HISTORY, USERS_ID, USERS_EMAIL, USERS_NICKNAME, USERS_PASSWORD,\
    USERS_AUTHENTICATED, HISTORY_ID, HISTORY_USER_ID, HISTORY_EXERCISE_ID, HISTORY_SETS, HISTORY_REPS, HISTORY_WEIGHT,\
    HISTORY_DATE, TAXONOMY_NAME, TAXONOMY_IS_BACK, TAXONOMY_IS_CHEST, TAXONOMY_IS_SHOULDERS, TAXONOMY_IS_BICEPS,\
    TAXONOMY_IS_TRICEPS, TAXONOMY_IS_LEGS, TAXONOMY_IS_CORE, TAXONOMY_IS_BALANCE, TAXONOMY_IS_CARDIO,\
    TAXONOMY_IS_WEIGHT_PER_HAND, TAXONOMY_ID
from app.models import Users, RepExercisesTaxonomy, RepExercisesHistory


class UtilitiesTests(unittest.TestCase):
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
            USERS_ID: test_id,
            USERS_EMAIL: test_email,
            USERS_NICKNAME: test_nickname,
            USERS_PASSWORD: test_password,
            USERS_AUTHENTICATED: False
        }

        self.assertDictEqual(result, expected_result)

    def test_taxonomy_obj_to_dict(self):
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

        taxonomy_obj.id = test_id

        result = _taxonomy_obj_to_dict(taxonomy_obj)

        expected_result = {
            TAXONOMY_ID: test_id,
            TAXONOMY_NAME: test_name,
            TAXONOMY_IS_BACK: test_is_back,
            TAXONOMY_IS_CHEST: test_is_chest,
            TAXONOMY_IS_SHOULDERS: test_is_shoulders,
            TAXONOMY_IS_BICEPS: test_is_biceps,
            TAXONOMY_IS_TRICEPS: test_is_triceps,
            TAXONOMY_IS_LEGS: test_is_legs,
            TAXONOMY_IS_CORE: test_is_core,
            TAXONOMY_IS_BALANCE: test_is_balance,
            TAXONOMY_IS_CARDIO: test_is_cardio,
            TAXONOMY_IS_WEIGHT_PER_HAND: test_is_weight_per_hand
        }

        self.assertDictEqual(result, expected_result)

    def test_history_obj_to_dict(self):
        pass

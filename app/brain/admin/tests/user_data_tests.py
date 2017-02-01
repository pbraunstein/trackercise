import unittest
from datetime import date

from app.brain.admin.user_data import UserData
from models import RepExercisesHistory


class UserDataTests(unittest.TestCase):
    def test_get_taxonomies_for_exercises(self):
        test_exercises = [
            RepExercisesHistory(
                user_id=1,
                exercise_id=42,
                sets=1,
                reps=23,
                weight=12,
                exercise_date=date.today()
            ),
            RepExercisesHistory(
                user_id=1,
                exercise_id=43,
                sets=1,
                reps=23,
                weight=12,
                exercise_date=date.today()
            ),
            RepExercisesHistory(
                user_id=1,
                exercise_id=44,
                sets=1,
                reps=23,
                weight=12,
                exercise_date=date.today()
            )
        ]

        resultant_exercise_ids = UserData._convert_rep_exercises_to_exercise_ids(test_exercises)
        expected_exercise_ids = [42, 43, 44]

        self.assertListEqual(resultant_exercise_ids, expected_exercise_ids)

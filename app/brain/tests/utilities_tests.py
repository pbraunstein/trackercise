import unittest
from datetime import date

from app.brain.utilities import prepare_history_entry
from app.models import RepExercisesHistory


class UtilitiesTests(unittest.TestCase):
    def test_prepare_history_entry_stringifies_date(self):
        test_entry = RepExercisesHistory(
            user_id=1,
            exercise_id=12,
            sets=1,
            reps=10,
            weight=20,
            exercise_date=date.today()
        )
        test_entry = prepare_history_entry(test_entry)
        self.assertIsInstance(test_entry.date, str)

from datetime import date
import unittest

import app
from brain.admin.all_data import AllData
from models import RepExercisesHistory


class AllDataTests(unittest.TestCase):
    def test_prepare_history_entry_stringifies_date(self):
        test_entry = RepExercisesHistory(
            user_id=1,
            exercise_id=12,
            sets=1,
            reps=10,
            weight=20,
            date=date.today()
        )
        test_entry = AllData._prepare_history_entry(test_entry)
        self.assertIsInstance(test_entry.date, str)

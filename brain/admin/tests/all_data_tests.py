import unittest

import app  # otherwise broken by circular imports :(
from brain.admin.all_data import AllData
from models import RepExercisesHistory, RepExercisesTaxonomy


class AllDataTests(unittest.TestCase):
    def test_prepare_taxonomy_entry_debooleanizes(self):
        exercise_name = 'test_awesomeness_exercise'
        test_entry = RepExercisesTaxonomy(
            name=exercise_name,
            is_back=True,
            is_chest=False,
            is_shoulders=True,
            is_biceps=True,
            is_triceps=False,
            is_legs=False,
            is_core=True,
            is_balance=True,
            is_cardio=False,
            is_weight_per_hand=False
        )

        new_entry = AllData._prepare_taxonomy_entry(test_entry)

        self.assertEqual(new_entry.name, exercise_name)
        self.assertEqual(new_entry.is_back, 'YES')
        self.assertEqual(new_entry.is_chest, 'NO')
        self.assertEqual(new_entry.is_shoulders, 'YES')
        self.assertEqual(new_entry.is_biceps, 'YES')
        self.assertEqual(new_entry.is_triceps, 'NO')
        self.assertEqual(new_entry.is_legs, 'NO')
        self.assertEqual(new_entry.is_core, 'YES')
        self.assertEqual(new_entry.is_balance, 'YES')
        self.assertEqual(new_entry.is_cardio, 'NO')
        self.assertEqual(new_entry.is_weight_per_hand, 'NO')

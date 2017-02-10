from datetime import date

from app.models import RepExercisesHistory, RepExercisesTaxonomy
from app.service import RepExercisesHistoryService, RepExercisesTaxonomyService, UsersService
from app.service_tests.service_test_case import ServiceTestCase


class RepExercisesHistoryTests(ServiceTestCase):
    def setUp(self):
        super(RepExercisesHistoryTests, self).setUp()
        UsersService.add_user_to_database('p@p.p', 'Patrick', 'pass')
        UsersService.add_user_to_database('j@j.j', 'Jaytrick', 'pass')
        RepExercisesTaxonomyService.add_entry_to_db(
            RepExercisesTaxonomy(
                name='test_rows',
                is_back=True,
                is_chest=False,
                is_shoulders=True,
                is_biceps=True,
                is_triceps=False,
                is_legs=False,
                is_core=True,
                is_balance=False,
                is_cardio=False,
                is_weight_per_hand=True
            )
        )
        RepExercisesTaxonomyService.add_entry_to_db(
            RepExercisesTaxonomy(
                name='test_press',
                is_back=False,
                is_chest=True,
                is_shoulders=True,
                is_biceps=False,
                is_triceps=True,
                is_legs=False,
                is_core=True,
                is_balance=False,
                is_cardio=False,
                is_weight_per_hand=True
            )
        )

    def test_add_entry_to_db(self):
        entry_to_add = RepExercisesHistory(
            user_id=2,
            exercise_id=1,
            sets=11,
            reps=23,
            weight=12.5,
            date=date(year=1990, month=12, day=23)
        )

        RepExercisesHistoryService.add_entry_to_db(entry_to_add)
        actual_entry = list(RepExercisesHistory.query.all())[0]
        self.assertEqual(actual_entry, entry_to_add)

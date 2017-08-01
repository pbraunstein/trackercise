from datetime import date

from app.models import RepExercisesHistory, RepExercisesTaxonomy, Users
from app.service import RepExercisesHistoryService, RepExercisesTaxonomyService, UsersService
from app.service_tests.service_test_case import ServiceTestCase


class RepExercisesHistoryTests(ServiceTestCase):
    def setUp(self):
        super(RepExercisesHistoryTests, self).setUp()

        # sample users for tests
        user_1 = Users('p@p.p', 'Patrick', 'pass')
        user_2 = Users('j@j.j', 'Jaytrick', 'pass')
        UsersService.add_user_to_database(user_1)
        UsersService.add_user_to_database(user_2)

        # sample exercises for tests
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

    # add_entry_to_db tests #
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

    # get_list_of_all_history tests #
    def test_get_list_of_all_history_no_history(self):
        expected_list = []
        actual_list = RepExercisesHistoryService.get_list_of_all_history()
        self.assertListEqual(actual_list, expected_list)

    def test_get_list_of_all_history_one_entry(self):
        entry_1 = RepExercisesHistory(
            user_id=2,
            exercise_id=1,
            sets=11,
            reps=23,
            weight=12.5,
            date=date(year=1990, month=12, day=23)
        )

        RepExercisesHistoryService.add_entry_to_db(entry_1)

        expected_list = [entry_1]
        actual_list = RepExercisesHistoryService.get_list_of_all_history()

        self.assertListEqual(actual_list, expected_list)

    def test_get_list_of_all_history_multiple_entries(self):
        expected_list = [
            RepExercisesHistory(
                user_id=1,
                exercise_id=1,
                sets=11,
                reps=23,
                weight=12.5,
                date=date(year=1990, month=12, day=23)
            ),
            RepExercisesHistory(
                user_id=2,
                exercise_id=2,
                sets=11,
                reps=23,
                weight=12.5,
                date=date(year=1890, month=12, day=23)
            ),
            RepExercisesHistory(
                user_id=2,
                exercise_id=1,
                sets=11,
                reps=23,
                weight=12.5,
                date=date(year=1997, month=12, day=23)
            )
        ]

        # add in entries
        RepExercisesHistoryService.add_entry_to_db(expected_list[0])
        RepExercisesHistoryService.add_entry_to_db(expected_list[1])
        RepExercisesHistoryService.add_entry_to_db(expected_list[2])

        actual_list = RepExercisesHistoryService.get_list_of_all_history()

        # no guarantee about ordering is made
        self.assertListEqual(sorted(actual_list, key=self._sort_key_date),
                             sorted(expected_list, key=self._sort_key_date))

    # get_list_of_users_exercises tests #
    def test_get_list_of_users_exercises_no_exercises(self):
        entry_1 = RepExercisesHistory(
            user_id=2,
            exercise_id=1,
            sets=11,
            reps=23,
            weight=12.5,
            date=date(year=1990, month=12, day=23)
        )
        entry_2 = RepExercisesHistory(
            user_id=2,
            exercise_id=2,
            sets=11,
            reps=23,
            weight=12,
            date=date(year=1990, month=11, day=23)
        )

        RepExercisesHistoryService.add_entry_to_db(entry_1)
        RepExercisesHistoryService.add_entry_to_db(entry_2)

        expected_list = []
        actual_list = RepExercisesHistoryService.get_list_of_users_exercises(1)

        self.assertListEqual(actual_list, expected_list)

    def test_get_list_of_users_exercises_pulls_correct_exercises(self):
        entry_1 = RepExercisesHistory(
            user_id=2,
            exercise_id=2,
            sets=11,
            reps=23,
            weight=12.5,
            date=date(year=1890, month=11, day=23)
        )
        entry_2 = RepExercisesHistory(
            user_id=1,
            exercise_id=1,
            sets=11,
            reps=23,
            weight=12.5,
            date=date(year=1890, month=11, day=29)
        )
        entry_3 = RepExercisesHistory(
            user_id=2,
            exercise_id=2,
            sets=11,
            reps=25,
            weight=12.5,
            date=date(year=1890, month=11, day=13)
        )

        RepExercisesHistoryService.add_entry_to_db(entry_1)
        RepExercisesHistoryService.add_entry_to_db(entry_2)
        RepExercisesHistoryService.add_entry_to_db(entry_3)

        expected_results = [entry_1, entry_3]  # entry_2 was done by a different user
        actual_results = RepExercisesHistoryService.get_list_of_users_exercises(2)

        # no guarantee about ordering is made
        self.assertListEqual(sorted(actual_results, key=self._sort_key_date),
                             sorted(expected_results, key=self._sort_key_date))

    # get_user_history_by_exercise tests #
    def test_get_user_history_by_exercise_empty_db(self):
        expected_results = []
        actual_results = RepExercisesHistoryService.get_user_history_by_exercise(user_id=1, exercise_id=2)

        self.assertListEqual(actual_results, expected_results)

    def test_get_user_history_by_exercise_user_not_done_that_exercise(self):
        entry_1 = RepExercisesHistory(
            user_id=2,
            exercise_id=2,
            sets=11,
            reps=23,
            weight=12.5,
            date=date(year=1890, month=11, day=23)
        )
        entry_2 = RepExercisesHistory(
            user_id=1,
            exercise_id=1,
            sets=11,
            reps=23,
            weight=12.5,
            date=date(year=1890, month=11, day=29)
        )

        RepExercisesHistoryService.add_entry_to_db(entry_1)
        RepExercisesHistoryService.add_entry_to_db(entry_2)

        expected_results = []
        actual_results = RepExercisesHistoryService.get_user_history_by_exercise(user_id=1, exercise_id=2)

        self.assertListEqual(actual_results, expected_results)

    def test_get_user_history_by_exercise_user_did_that_exercise(self):
        entry_1 = RepExercisesHistory(
            user_id=2,
            exercise_id=2,
            sets=11,
            reps=23,
            weight=12.5,
            date=date(year=1890, month=11, day=23)
        )
        entry_2 = RepExercisesHistory(
            user_id=1,
            exercise_id=1,
            sets=11,
            reps=23,
            weight=12.5,
            date=date(year=1890, month=11, day=29)
        )
        entry_3 = RepExercisesHistory(
            user_id=2,
            exercise_id=2,
            sets=11,
            reps=23,
            weight=12.5,
            date=date(year=1892, month=11, day=29)
        )

        RepExercisesHistoryService.add_entry_to_db(entry_1)
        RepExercisesHistoryService.add_entry_to_db(entry_2)
        RepExercisesHistoryService.add_entry_to_db(entry_3)

        expected_results = [entry_1, entry_3]
        actual_results = RepExercisesHistoryService.get_user_history_by_exercise(user_id=2, exercise_id=2)

        # no guarantee about ordering is made
        self.assertListEqual(sorted(actual_results, key=self._sort_key_date), sorted(expected_results, key=self._sort_key_date))

    def test_get_user_history_by_exercise_different_user_did_that_exercise(self):
        entry_1 = RepExercisesHistory(
            user_id=2,
            exercise_id=2,
            sets=11,
            reps=23,
            weight=12.5,
            date=date(year=1890, month=11, day=23)
        )
        entry_2 = RepExercisesHistory(
            user_id=1,
            exercise_id=1,
            sets=11,
            reps=23,
            weight=12.5,
            date=date(year=1890, month=11, day=29)
        )
        entry_3 = RepExercisesHistory(
            user_id=2,
            exercise_id=2,
            sets=11,
            reps=23,
            weight=12.5,
            date=date(year=1892, month=11, day=29)
        )

        RepExercisesHistoryService.add_entry_to_db(entry_1)
        RepExercisesHistoryService.add_entry_to_db(entry_2)
        RepExercisesHistoryService.add_entry_to_db(entry_3)

        expected_results = []
        actual_results = RepExercisesHistoryService.get_user_history_by_exercise(1, 2)

        self.assertListEqual(actual_results, expected_results)

    # get_user_history_by_date tests #
    def test_get_user_history_by_date_empty_db(self):
        expected_results = []
        actual_results = RepExercisesHistoryService.get_user_history_by_date(1, '2017-07-20')

        self.assertListEqual(actual_results, expected_results)

    def test_get_user_history_by_date_no_match(self):
        entry_1 = RepExercisesHistory(
            user_id=2,
            exercise_id=2,
            sets=11,
            reps=23,
            weight=12.5,
            date=date(year=1890, month=11, day=23)
        )
        entry_2 = RepExercisesHistory(
            user_id=1,
            exercise_id=1,
            sets=11,
            reps=23,
            weight=12.5,
            date=date(year=1890, month=11, day=29)
        )
        entry_3 = RepExercisesHistory(
            user_id=2,
            exercise_id=2,
            sets=11,
            reps=23,
            weight=12.5,
            date=date(year=1892, month=11, day=29)
        )

        RepExercisesHistoryService.add_entry_to_db(entry_1)
        RepExercisesHistoryService.add_entry_to_db(entry_2)
        RepExercisesHistoryService.add_entry_to_db(entry_3)

        expected_results = []
        actual_results = RepExercisesHistoryService.get_user_history_by_date(1, '1892-11-23')
        self.assertListEqual(actual_results, expected_results)

    def test_get_user_history_by_date_match(self):
        entry_1 = RepExercisesHistory(
            user_id=1,
            exercise_id=2,
            sets=11,
            reps=23,
            weight=12.5,
            date=date(year=1890, month=11, day=23)
        )
        entry_2 = RepExercisesHistory(
            user_id=1,
            exercise_id=1,
            sets=11,
            reps=23,
            weight=12.5,
            date=date(year=1890, month=11, day=23)
        )
        entry_3 = RepExercisesHistory(
            user_id=2,
            exercise_id=2,
            sets=11,
            reps=23,
            weight=12.5,
            date=date(year=1892, month=11, day=29)
        )

        RepExercisesHistoryService.add_entry_to_db(entry_1)
        RepExercisesHistoryService.add_entry_to_db(entry_2)
        RepExercisesHistoryService.add_entry_to_db(entry_3)

        expected_results = [entry_1, entry_2]
        actual_results = RepExercisesHistoryService.get_user_history_by_date(1, '1890-11-23')

        self.assertListEqual(sorted(actual_results, key=self._sort_key_exercise_id),
                             sorted(expected_results, key=self._sort_key_exercise_id))

    @staticmethod
    def _sort_key_date(x):
        return x.date

    @staticmethod
    def _sort_key_exercise_id(x):
        return x.exercise_id

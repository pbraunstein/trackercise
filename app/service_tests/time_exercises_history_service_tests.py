from datetime import date
from app.models import TimeExercisesHistory, TimeExercisesTaxonomy, Users
from app.service import TimeExercisesHistoryService, TimeExercisesTaxonomyService, UsersService
from app.service_tests.service_test_case import ServiceTestCase


class TimeExercisesHistoryTests(ServiceTestCase):
    def setUp(self):
        super(TimeExercisesHistoryTests, self).setUp()

        # sample users for tests
        user_1 = Users('p@p.p', 'Patrick', 'pass')
        user_2 = Users('j@j.j', 'Jaytrick', 'pass')
        UsersService.add_user_to_database(user_1)
        UsersService.add_user_to_database(user_2)

        # sample exercises for tests
        TimeExercisesTaxonomyService.add_entry_to_db(
            TimeExercisesTaxonomy(name='rowing')
        )
        TimeExercisesTaxonomyService.add_entry_to_db(
            TimeExercisesTaxonomy(name='running')
        )
        TimeExercisesTaxonomyService.add_entry_to_db(
            TimeExercisesTaxonomy(name='elliptical')
        )

    # add_entry_to_db tests #
    def test_add_entry_to_db(self):
        expected_entry = TimeExercisesHistory(
            user_id=2,
            exercise_id=1,
            distance=2.3,
            duration=34.12,
            exercise_date=date(year=2016, month=12, day=31)
        )

        TimeExercisesHistoryService.add_entry_to_db(expected_entry)
        actual_entry = list(TimeExercisesHistory.query.all())[0]
        self.assertEqual(actual_entry, expected_entry)

    # get_list_of_all_history tests #
    def test_get_list_of_all_history_no_entries(self):
        expected_list = []
        actual_list = TimeExercisesHistoryService.get_list_of_all_history()
        self.assertListEqual(actual_list, expected_list)

    def test_get_list_of_all_history_one_entry(self):
        entry_1 = TimeExercisesHistory(
            user_id=2,
            exercise_id=1,
            distance=2.3,
            duration=34.12,
            exercise_date=date(year=2016, month=12, day=31)
        )

        TimeExercisesHistoryService.add_entry_to_db(entry_1)
        expected_list = [entry_1]
        actual_list = TimeExercisesHistoryService.get_list_of_all_history()

        self.assertListEqual(actual_list, expected_list)

    def test_get_list_of_all_history_multiple_entries(self):
        expected_list = [
            TimeExercisesHistory(
                user_id=2,
                exercise_id=1,
                distance=2.3,
                duration=34.12,
                exercise_date=date(year=2016, month=12, day=31)
            ),
            TimeExercisesHistory(
                user_id=2,
                exercise_id=2,
                distance=4.0,
                duration=38,
                exercise_date=date(year=2016, month=12, day=30)
            ),
            TimeExercisesHistory(
                user_id=2,
                exercise_id=3,
                distance=2.0,
                duration=24.12,
                exercise_date=date(year=2016, month=12, day=15)
            )
        ]

        TimeExercisesHistoryService.add_entry_to_db(expected_list[0])
        TimeExercisesHistoryService.add_entry_to_db(expected_list[1])
        TimeExercisesHistoryService.add_entry_to_db(expected_list[2])

        actual_list = TimeExercisesHistoryService.get_list_of_all_history()

        # no guarantee about ordering is made
        self.assertListEqual(sorted(actual_list, key=self._sort_key_date),
                             sorted(expected_list, key=self._sort_key_date))

    # get_list_of_users_exercises tests #
    def test_get_list_of_users_exercises_no_exercises(self):
        entry_1 = TimeExercisesHistory(
            user_id=2,
            exercise_id=1,
            distance=2.3,
            duration=34.12,
            exercise_date=date(year=2016, month=12, day=31)
        )
        entry_2 = TimeExercisesHistory(
            user_id=2,
            exercise_id=2,
            distance=4.0,
            duration=38,
            exercise_date=date(year=2016, month=12, day=30)
        )

        TimeExercisesHistoryService.add_entry_to_db(entry_1)
        TimeExercisesHistoryService.add_entry_to_db(entry_2)

        expected_list = []
        actual_list = TimeExercisesHistoryService.get_list_of_users_exercises(1)

        self.assertListEqual(actual_list, expected_list)

    def test_get_list_of_users_exercises_pulls_correct_exercises(self):
        entry_1 = TimeExercisesHistory(
            user_id=2,
            exercise_id=1,
            distance=2.3,
            duration=34.12,
            exercise_date=date(year=2016, month=12, day=31)
        )
        entry_2 = TimeExercisesHistory(
            user_id=1,
            exercise_id=2,
            distance=4.0,
            duration=38,
            exercise_date=date(year=2016, month=12, day=30)
        )
        entry_3 = TimeExercisesHistory(
            user_id=2,
            exercise_id=3,
            distance=2.0,
            duration=24.12,
            exercise_date=date(year=2016, month=12, day=15)
        )

        TimeExercisesHistoryService.add_entry_to_db(entry_1)
        TimeExercisesHistoryService.add_entry_to_db(entry_2)
        TimeExercisesHistoryService.add_entry_to_db(entry_3)

        expected_results = [entry_1, entry_3] # entry_2 was done by a different user
        actual_results = TimeExercisesHistoryService.get_list_of_users_exercises(2)

        # no guarantee about ordering is made
        self.assertListEqual(sorted(actual_results, key=self._sort_key_date),
                             sorted(expected_results, key=self._sort_key_date))

    @staticmethod
    def _sort_key_date(x):
        return x.exercise_date

    @staticmethod
    def _sort_key_exercise_id(x):
        return x.exercise_id

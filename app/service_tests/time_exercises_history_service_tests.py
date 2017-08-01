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

from app.models import TimeExercisesTaxonomy
from app.service import TimeExercisesTaxonomyService
from app.service_tests.service_test_case import ServiceTestCase


class TimeExercisesTaxonomyTests(ServiceTestCase):
    # add_entry_to_db tests #
    def test_add_entry_to_db(self):
        expected_result = TimeExercisesTaxonomy(name='rowing')

        TimeExercisesTaxonomyService.add_entry_to_db(expected_result)

        actual_result = list(TimeExercisesTaxonomy.query.all())[0]
        self.assertEqual(actual_result, expected_result)

    # get_list_of_all_exercises tests #
    def test_get_list_of_all_exercises_no_exercises(self):
        expected_results = []
        actual_results = TimeExercisesTaxonomyService.get_list_of_all_exercises()
        self.assertEqual(actual_results, expected_results)

    def test_get_list_of_all_exercises_one_exercise(self):
        entry_1 = TimeExercisesTaxonomy(name='running')

        TimeExercisesTaxonomyService.add_entry_to_db(entry_1)
        expected_results = [entry_1]
        actual_results = TimeExercisesTaxonomyService.get_list_of_all_exercises()

        self.assertListEqual(actual_results, expected_results)

    def test_get_list_of_all_exercises_multiple_exercises(self):
        entry_1 = TimeExercisesTaxonomy(name='running')
        entry_2 = TimeExercisesTaxonomy(name='rowing')
        entry_3 = TimeExercisesTaxonomy(name='eliptical')

        TimeExercisesTaxonomyService.add_entry_to_db(entry_1)
        TimeExercisesTaxonomyService.add_entry_to_db(entry_2)
        TimeExercisesTaxonomyService.add_entry_to_db(entry_3)

        expected_results = [entry_1, entry_2, entry_3]
        actual_results = TimeExercisesTaxonomyService.get_list_of_all_exercises()

        # no guarantee of ordering made
        self.assertListEqual(sorted(actual_results, key=self._sort_key), sorted(expected_results, key=self._sort_key))

    @staticmethod
    def _sort_key(x):
        return x.name

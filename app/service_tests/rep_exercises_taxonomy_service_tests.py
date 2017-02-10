from app.models import RepExercisesTaxonomy
from app.service import RepExercisesTaxonomyService
from app.service_tests.service_test_case import ServiceTestCase


class RepExercisesTaxonomyTests(ServiceTestCase):
    # add_entry_to_db tests #
    def test_add_entry_to_db(self):
        expected_result = RepExercisesTaxonomy(
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

        RepExercisesTaxonomyService.add_entry_to_db(expected_result)

        actual_result = list(RepExercisesTaxonomy.query.all())[0]

        self.assertEqual(actual_result, expected_result)

    # get_list_of_all_exercises tests #
    def test_get_list_of_all_exercises_no_exercises(self):
        expected_results = []
        actual_results = RepExercisesTaxonomyService.get_list_of_all_exercises()
        self.assertListEqual(actual_results, expected_results)

    def test_get_list_of_all_exercises_one_exercise(self):
        pass

    def test_get_list_of_all_exercises_multiple_exercises(self):
        pass

    @staticmethod
    def _sort_key(x):
        return x.name

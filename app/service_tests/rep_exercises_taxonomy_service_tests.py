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
        entry_1 = RepExercisesTaxonomy(
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

        RepExercisesTaxonomyService.add_entry_to_db(entry_1)
        expected_results = [entry_1]
        actual_results = RepExercisesTaxonomyService.get_list_of_all_exercises()

        self.assertListEqual(actual_results, expected_results)

    def test_get_list_of_all_exercises_multiple_exercises(self):
        entry_1 = RepExercisesTaxonomy(
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
        entry_2 = RepExercisesTaxonomy(
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
        entry_3 = RepExercisesTaxonomy(
            name='test_shrugs_bosu',
            is_back=True,
            is_chest=False,
            is_shoulders=True,
            is_biceps=False,
            is_triceps=False,
            is_legs=False,
            is_core=True,
            is_balance=True,
            is_cardio=False,
            is_weight_per_hand=True
        )

        RepExercisesTaxonomyService.add_entry_to_db(entry_1)
        RepExercisesTaxonomyService.add_entry_to_db(entry_2)
        RepExercisesTaxonomyService.add_entry_to_db(entry_3)

        expected_results = [entry_1, entry_2, entry_3]
        actual_results = RepExercisesTaxonomyService.get_list_of_all_exercises()

        self.assertListEqual(sorted(actual_results, key=self._sort_key), sorted(expected_results, key=self._sort_key))

    # get_list_of_taxonomies_by_exercise_ids #
    def test_get_list_of_taxonomies_by_exercise_ids(self):
        entry_1 = RepExercisesTaxonomy(
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
        entry_2 = RepExercisesTaxonomy(
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
        entry_3 = RepExercisesTaxonomy(
            name='test_shrugs_bosu',
            is_back=True,
            is_chest=False,
            is_shoulders=True,
            is_biceps=False,
            is_triceps=False,
            is_legs=False,
            is_core=True,
            is_balance=True,
            is_cardio=False,
            is_weight_per_hand=True
        )

        RepExercisesTaxonomyService.add_entry_to_db(entry_1)
        RepExercisesTaxonomyService.add_entry_to_db(entry_2)
        RepExercisesTaxonomyService.add_entry_to_db(entry_3)

        expected_results = [entry_1, entry_3]
        actual_results = RepExercisesTaxonomyService.get_list_of_taxonomies_by_exercise_ids([1, 3])

        # no guarantee of ordering made
        self.assertListEqual(sorted(actual_results, key=self._sort_key), sorted(expected_results, key=self._sort_key))

    @staticmethod
    def _sort_key(x):
        return x.name

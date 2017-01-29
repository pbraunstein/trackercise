from service import RepExercisesHistoryService, RepExercisesTaxonomyService


class RepExercisesManagement(object):
    @classmethod
    def get_valid_id_exercise_pairs(cls):
        valid_exercises = RepExercisesTaxonomyService.get_list_of_all_exercises()
        id_exercise_pairs = [(x.id, x.name) for x in valid_exercises]

        return id_exercise_pairs

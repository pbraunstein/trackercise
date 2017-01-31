from service import RepExercisesHistoryService, RepExercisesTaxonomyService
from models import RepExercisesHistory


class RepExercisesManagement(object):
    @staticmethod
    def get_valid_id_exercise_pairs():
        valid_exercises = RepExercisesTaxonomyService.get_list_of_all_exercises()
        id_exercise_pairs = [(str(x.id), x.name) for x in valid_exercises]
        id_exercise_pairs_sorted = sorted(id_exercise_pairs, key=lambda y: y[1])

        return id_exercise_pairs_sorted

    @staticmethod
    def submit_history_entry(user_id, exercise_id, sets, reps, weight, exercise_date):
        entry_to_add = RepExercisesHistory(
            user_id=user_id,
            exercise_id=exercise_id,
            sets=sets,
            reps=reps,
            weight=weight,
            exercise_date=exercise_date
        )
        RepExercisesHistoryService.add_entry_to_db(entry_to_add)

        return entry_to_add

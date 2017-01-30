from datetime import date

from service import RepExercisesHistoryService, RepExercisesTaxonomyService
from models import RepExercisesHistory


class RepExercisesManagement(object):
    @staticmethod
    def get_valid_id_exercise_pairs():
        valid_exercises = RepExercisesTaxonomyService.get_list_of_all_exercises()
        id_exercise_pairs = [(str(x.id), x.name) for x in valid_exercises]

        return id_exercise_pairs

    @staticmethod
    def submit_history_entry(user_id, exercise_id, sets, reps, weight):
        entry_to_add = RepExercisesHistory(
            user_id=user_id,
            exercise_id=exercise_id,
            sets=sets,
            reps=reps,
            weight=weight,
            date=date.today()
        )
        RepExercisesHistoryService.add_entry_to_db(entry_to_add)

        return entry_to_add

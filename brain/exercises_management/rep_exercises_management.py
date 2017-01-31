from service import RepExercisesHistoryService, RepExercisesTaxonomyService
from models import RepExercisesHistory


class RepExercisesManagement(object):
    """
    Interactions with the RepExercises both Histories and Taxonomies

    I N T E R F A C E   G U A R A N T E E D
    ---------------------------------------
    get_valid_id_exercise_pairs():
        -- Returns list of tuples of all available rep exercise taxonomies sorted by the name of the exercise
            [(exercise.id, exercise.name), ...]

    submit_history_entry(user_id, exercise_id, sets, reps, weight, exercise_date):
        -- Adds a RepExerciseHistory to the database for the user whose user_id is passed in
    """
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
            date=exercise_date
        )
        RepExercisesHistoryService.add_entry_to_db(entry_to_add)

        return entry_to_add

from app.models import TimeExercisesTaxonomy, TimeExercisesHistory
from app.service import TimeExercisesTaxonomyService, TimeExercisesHistoryService


class TimeExercisesManagement(object):
    """
    Interactions with TimeExercises both Histories and Taxonomies

    I N T E R F A C E   G U A R AN T E E D
    --------------------------------------
    get_valid_id_exercise_pairs():
    -- Returns list of tuples of all available time exercise taxonomies sorted by the name of the exercise
            [(exercise.id, exercise.name), ...]

    get_user_history_by_exercise_id(user_id, exercise_id):
        -- Returns a chronological list of the TimeExercisesHistory of type exercise_id that user_id has entered
            [TimeExercisesHistory(), ...]
        -- Guarantees that the entries are returned in chronological order

    get_user_history_by_date(user_id, exercise_date):
        -- Returns a list of the TimExercisesHistory that occurred on date exercise_date for user_id
            [TimeExercisesHistory(), ...]
        -- Guarantees that the entries are sorted in ascending order of exercise_id (this is somewhat arbitrary)

    submit_history_entry(user_id, exercise_id, distance, duration, exercise_date):
        -- Creates and adds a TimeExercisesHistory to the database for the user_id that's passed in
        -- Returns the added entry


    submit_taxonomy_entry(name):
        -- Creates and adds a TimeExercisesTaxonomy to the database. Returns the added entry
    """
    @staticmethod
    def get_valid_id_exercise_pairs():
        valid_exercises = TimeExercisesTaxonomyService.get_list_of_all_exercises()
        id_exercise_pairs = [(str(x.id), x.name.upper()) for x in valid_exercises]
        return sorted(id_exercise_pairs, key=lambda y: y[1])

    @staticmethod
    def get_user_history_by_exercise_id(user_id, exercise_id):
        return sorted(
            TimeExercisesHistoryService.get_user_history_by_exercise(user_id, exercise_id),
            key=lambda x: x.exercise_date
        )

    @staticmethod
    def get_user_history_by_date(user_id, exercise_date):
        return sorted(
            TimeExercisesHistoryService.get_user_history_by_date(user_id, exercise_date),
            key=lambda x: x.exercise_id
        )

    @staticmethod
    def submit_history_entry(user_id, exercise_id, distance, duration, exercise_date):
        entry_to_add = TimeExercisesHistory(
            user_id=user_id,
            exercise_id=exercise_id,
            distance=distance,
            duration=duration,
            exercise_date=exercise_date
        )

        TimeExercisesHistoryService.add_entry_to_db(entry_to_add)

        return entry_to_add

    @staticmethod
    def submit_taxonomy_entry(name):
        entry_to_add = TimeExercisesTaxonomy(name=name)

        TimeExercisesTaxonomyService.add_entry_to_db(entry_to_add)

        return entry_to_add

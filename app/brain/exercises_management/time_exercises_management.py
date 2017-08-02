from app.models import TimeExercisesTaxonomy, TimeExercisesHistory
from app.service import TimeExercisesTaxonomyService, TimeExercisesHistoryService


class TimeExercisesManagement(object):
    """
    Interactions with TimeExercises both Histories and Taxonomies

    I N T E R F A C E   G U A R AN T E E D
    --------------------------------------
    submit_history_entry(user_id, exercise_id, distance, duration, exercise_date):
        -- Creates and adds a TimeExercisesHistory to the database for the user_id that's passed in
        -- Returns the added entry


    submit_taxonomy_entry(name):
        -- Creates and adds a TimeExercisesTaxonomy to the database. Returns the added entry
    """
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

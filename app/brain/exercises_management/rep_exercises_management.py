from app.brain.custom_exceptions import ThisShouldNeverHappenException
from app.models import RepExercisesHistory, RepExercisesTaxonomy
from app.service import RepExercisesHistoryService, RepExercisesTaxonomyService


class RepExercisesManagement(object):
    """
    Interactions with the RepExercises both Histories and Taxonomies

    I N T E R F A C E   G U A R A N T E E D
    ---------------------------------------
    get_valid_id_exercise_pairs():
        -- Returns list of tuples of all available rep exercise taxonomies sorted by the name of the exercise
            [(exercise.id, exercise.name), ...]

    get_user_history_by_exercise_id(user_id, exercise_id):
        -- Returns a chronological list of the RepExercisesHistory of type exercise_id that user_id has entered
            [RepExercisesHistory(), ...]
        -- Guarantees that the entries are in chronological order

    get_user_history_by_date(user_id, exercise_date):
        -- Returns a list of the RepExercisesHistory that occurred on date exercise_date for user_id
            [RepExercisesHistory(), ...]
        -- Guarantees that the entries are sorted in ascending order of exercise_id (this is somewhat arbitrary)

    submit_history_entry(user_id, exercise_id, sets, reps, weight, exercise_date):
        -- Creates and adds a RepExercisesHistory to the database for the user whose user_id is passed in
        -- Returns the added entry

    submit_taxonomy_entry(name, is_back, is_chest, is_shoulders, is_biceps, is_triceps, is_legs, is_core, is_balance,
        is_cardio, is_weight_per_hand):
        -- Creates and adds a RepExercisesTaxonomy to the database. Returns the added entry
    """
    @staticmethod
    def get_valid_id_exercise_pairs():
        valid_exercises = RepExercisesTaxonomyService.get_list_of_all_exercises()
        id_exercise_pairs = [(str(x.id), x.name) for x in valid_exercises]
        id_exercise_pairs_sorted = sorted(id_exercise_pairs, key=lambda y: y[1])

        return id_exercise_pairs_sorted

    @staticmethod
    def get_user_history_by_exercise_id(user_id, exercise_id):
        return sorted(
            RepExercisesHistoryService.get_user_history_by_exercise(user_id, exercise_id),
            key=lambda x: x.date
        )

    @staticmethod
    def get_user_history_by_date(user_id, exercise_date):
        return sorted(
            RepExercisesHistoryService.get_user_history_by_date(user_id, exercise_date),
            key=lambda x: x.exercise_id
        )

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

    @staticmethod
    def submit_taxonomy_entry(name, is_back, is_chest, is_shoulders, is_biceps, is_triceps, is_legs, is_core,
                              is_balance, is_cardio, is_weight_per_hand):
        entry_to_add = RepExercisesTaxonomy(
            name=name,
            is_back=is_back,
            is_chest=is_chest,
            is_shoulders=is_shoulders,
            is_biceps=is_biceps,
            is_triceps=is_triceps,
            is_legs=is_legs,
            is_core=is_core,
            is_balance=is_balance,
            is_cardio=is_cardio,
            is_weight_per_hand=is_weight_per_hand
        )
        RepExercisesTaxonomyService.add_entry_to_db(entry_to_add)

        return entry_to_add

    @staticmethod
    def convert_ts_strings_to_booleans(input_string):
        if input_string == 'false':
            return False
        elif input_string == 'true':
            return True
        else:
            raise ThisShouldNeverHappenException('Unexpected boolean value received')

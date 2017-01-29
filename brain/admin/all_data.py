from brain.utilities import prepare_history_entry
from service import UsersService, RepExercisesTaxonomyService, RepExercisesHistoryService


class AllData(object):
    """
    Returns all the data. This is only for debug, and it will break with scale

    I N T E R F A C E   G U A R A N T E E D
    ---------------------------------------
    get_all_data(cls):
        -- Returns a list of lists [users, taxonomy, history]
    """

    @classmethod
    def get_all_data(cls):
        user_results = UsersService.get_list_of_all_users()
        taxonomy_results = RepExercisesTaxonomyService.get_list_of_all_exercises()
        taxonomy_results = [cls._prepare_taxonomy_entry(x) for x in taxonomy_results]
        history_results = RepExercisesHistoryService.get_list_of_all_history()
        history_results = [prepare_history_entry(x) for x in history_results]
        return [user_results, taxonomy_results, history_results]


    @staticmethod
    def _prepare_taxonomy_entry(entry):
        """
        Turns boolean True or False to YES or NO for RepExercisesTaxonomy entry
        """

        def debooleanize(value):
            return 'YES' if value else 'NO'

        entry.is_back = debooleanize(entry.is_back)
        entry.is_chest = debooleanize(entry.is_chest)
        entry.is_shoulders = debooleanize(entry.is_shoulders)
        entry.is_biceps = debooleanize(entry.is_biceps)
        entry.is_triceps = debooleanize(entry.is_triceps)
        entry.is_legs = debooleanize(entry.is_legs)
        entry.is_core = debooleanize(entry.is_core)
        entry.is_balance = debooleanize(entry.is_balance)
        entry.is_cardio = debooleanize(entry.is_cardio)
        entry.is_weight_per_hand = debooleanize(entry.is_weight_per_hand)

        return entry

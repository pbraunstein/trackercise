from app.brain.utilities import prepare_history_entry
from app.constants import USERS_CONSTANTS, TAXONOMY_CONSTANTS, HISTORY_CONSTNATS
from app.service import UsersService, RepExercisesTaxonomyService, RepExercisesHistoryService


class AllData(object):
    """
    Returns all the data. This is only for debug, and it will break with scale

    I N T E R F A C E   G U A R A N T E E D
    ---------------------------------------
    get_all_data(cls):
        -- Returns a dictionary of all of data of users, taxonomy, and history
        -- {users: [Users, ...], taxonomy: [Taxonomy, ...], history: [History, ...]}
    """

    @classmethod
    def get_all_data(cls):
        all_results = {}
        user_results = UsersService.get_list_of_all_users()
        taxonomy_results = RepExercisesTaxonomyService.get_list_of_all_exercises()
        history_results = RepExercisesHistoryService.get_list_of_all_history()
        history_results = [prepare_history_entry(x) for x in history_results]
        all_results[USERS_CONSTANTS.NAME] = user_results
        all_results[TAXONOMY_CONSTANTS.GROUP_NAME] = taxonomy_results
        all_results[HISTORY_CONSTNATS.NAME] = history_results
        return all_results

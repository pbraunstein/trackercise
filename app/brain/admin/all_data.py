from app.brain.utilities import prepare_history_entry
from app.constants import USERS, TAXONOMY, HISTORY
from app.service import UsersService, RepExercisesTaxonomyService, RepExercisesHistoryService


class AllData(object):
    """
    Returns all the data. This is only for debug, and it will break with scale

    I N T E R F A C E   G U A R A N T E E D
    ---------------------------------------
    get_all_data(cls):
        -- Returns a dictionary of all of data of users, taxonomy, and history
        -- {users: [User, ...], taxonomy: [taxonomy, ...], history: [history, ...]}
    """

    @classmethod
    def get_all_data(cls):
        all_results = {}
        user_results = UsersService.get_list_of_all_users()
        taxonomy_results = RepExercisesTaxonomyService.get_list_of_all_exercises()
        history_results = RepExercisesHistoryService.get_list_of_all_history()
        history_results = [prepare_history_entry(x) for x in history_results]
        all_results[USERS] = user_results
        all_results[TAXONOMY] = taxonomy_results
        all_results[HISTORY] = history_results
        return all_results

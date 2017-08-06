import hashlib

from app.brain.custom_exceptions import ThisShouldNeverHappenException
from app.constants import USERS_CONSTANTS, TAXONOMY_CONSTANTS, HISTORY_CONSTANTS
from app.models import RepExercisesHistory, TimeExercisesHistory, RepExercisesTaxonomy, TimeExercisesTaxonomy


def hash_password(password):
    return hashlib.sha256(password).hexdigest()


def prepare_history_entry(entry):
    """
    Stringifies date of RepExercisesHistory entry
    """
    entry.date = str(entry.date)
    return entry


def all_data_to_dict(all_data):
    all_data[USERS_CONSTANTS.GROUP_NAME] = list_user_objs_to_list_dicts(all_data[USERS_CONSTANTS.GROUP_NAME])
    all_data[TAXONOMY_CONSTANTS.GROUP_NAME] = list_taxonomy_objs_to_dicts(all_data[TAXONOMY_CONSTANTS.GROUP_NAME])
    all_data[HISTORY_CONSTANTS.GROUP_NAME] = list_history_objs_to_dicts(all_data[HISTORY_CONSTANTS.GROUP_NAME])
    return all_data


def user_data_to_dict(user_data):
    user_data[HISTORY_CONSTANTS.GROUP_NAME] = list_history_objs_to_dicts(user_data[HISTORY_CONSTANTS.GROUP_NAME])
    user_data[TAXONOMY_CONSTANTS.GROUP_NAME] = list_taxonomy_objs_to_dicts(user_data[TAXONOMY_CONSTANTS.GROUP_NAME])
    return user_data


def list_user_objs_to_list_dicts(user_list):
    return [_user_obj_to_dict(x) for x in user_list]


def list_taxonomy_objs_to_dicts(taxonomy_list):
    return [_taxonomy_obj_to_dict(x) for x in taxonomy_list]


def list_history_objs_to_dicts(history_list):
    return [_history_obj_to_dict(x) for x in history_list]


def _user_obj_to_dict(user):
    """
    Converts a Users object (db model) into a dictionary
    """
    return {
        USERS_CONSTANTS.ID: user.id,
        USERS_CONSTANTS.EMAIL: user.email,
        USERS_CONSTANTS.NICKNAME: user.nickname,
        USERS_CONSTANTS.PASSWORD: user.password,
        USERS_CONSTANTS.AUTHENTICATED: user.authenticated
    }


def _taxonomy_obj_to_dict(taxonomy):
    """
    Converts a Taxonomy object into a dictionary. This method supports both RepExercisesTaxonomy
    and TimeExercisesTaxonomy objects.

    Throws ThisShouldNeverHappen exception if the arg passed in is neither RepExercisesTaxonomy nor
    TimeExercisesTaxonomy
    """
    if isinstance(taxonomy, RepExercisesTaxonomy):
        return {
            TAXONOMY_CONSTANTS.ID: taxonomy.id,
            TAXONOMY_CONSTANTS.NAME: taxonomy.name,
            TAXONOMY_CONSTANTS.IS_BACK: taxonomy.is_back,
            TAXONOMY_CONSTANTS.IS_CHEST: taxonomy.is_chest,
            TAXONOMY_CONSTANTS.IS_SHOULDERS: taxonomy.is_shoulders,
            TAXONOMY_CONSTANTS.IS_BICEPS: taxonomy.is_biceps,
            TAXONOMY_CONSTANTS.IS_TRICEPS: taxonomy.is_triceps,
            TAXONOMY_CONSTANTS.IS_LEGS: taxonomy.is_legs,
            TAXONOMY_CONSTANTS.IS_CORE: taxonomy.is_core,
            TAXONOMY_CONSTANTS.IS_BALANCE: taxonomy.is_balance,
            TAXONOMY_CONSTANTS.IS_CARDIO: taxonomy.is_cardio,
            TAXONOMY_CONSTANTS.IS_WEIGHT_PER_HAND: taxonomy.is_weight_per_hand
        }
    elif isinstance(taxonomy, TimeExercisesTaxonomy):
        return {
            TAXONOMY_CONSTANTS.ID: taxonomy.id,
            TAXONOMY_CONSTANTS.NAME: taxonomy.name
        }
    else:
        raise ThisShouldNeverHappenException('Unknow type passed to _taxonomy_obj_to_dict')


def _history_obj_to_dict(history):
    """
    Converts a history object to a dictionary. This method supports both RepExercisesHistory and TimeExercisesHistory
    objects.

    Throws ThisShouldNeverHappen exception if the arg passed in is neither RepExercisesHistory nor TimeExercisesHistory
    """
    if isinstance(history, RepExercisesHistory):
        return {
            HISTORY_CONSTANTS.ID: history.id,
            HISTORY_CONSTANTS.USER_ID: history.user_id,
            HISTORY_CONSTANTS.EXERCISE_ID: history.exercise_id,
            HISTORY_CONSTANTS.SETS: history.sets,
            HISTORY_CONSTANTS.REPS: history.reps,
            HISTORY_CONSTANTS.WEIGHT: history.weight,
            HISTORY_CONSTANTS.DATE: str(history.date)
        }
    elif isinstance(history, TimeExercisesHistory):
        return {
            HISTORY_CONSTANTS.ID: history.id,
            HISTORY_CONSTANTS.USER_ID: history.user_id,
            HISTORY_CONSTANTS.EXERCISE_ID: history.exercise_id,
            HISTORY_CONSTANTS.DISTANCE: history.distance,
            HISTORY_CONSTANTS.DURATION: history.duration,
            HISTORY_CONSTANTS.DATE: str(history.exercise_date)
        }
    else:
        raise ThisShouldNeverHappenException('Unknown type passed to _history_obj_to_dict')

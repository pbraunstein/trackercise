import hashlib

from app.constants import USERS_CONSTANTS, TAXONOMY_CONSTANTS, HISTORY_CONSTNATS


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
    all_data[HISTORY_CONSTNATS.GROUP_NAME] = list_history_objs_to_dicts(all_data[HISTORY_CONSTNATS.GROUP_NAME])
    return all_data


def user_data_to_dict(user_data):
    user_data[HISTORY_CONSTNATS.GROUP_NAME] = list_history_objs_to_dicts(user_data[HISTORY_CONSTNATS.GROUP_NAME])
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
    Converts a Taxonomy object (db model) into a dictionary
    """
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


def _history_obj_to_dict(history):
    """
    Converts a RepExercisesHistory object (db model) into a dictionary
    """
    return {
        HISTORY_CONSTNATS.ID: history.id,
        HISTORY_CONSTNATS.USER_ID: history.user_id,
        HISTORY_CONSTNATS.EXERCISE_ID: history.exercise_id,
        HISTORY_CONSTNATS.SETS: history.sets,
        HISTORY_CONSTNATS.REPS: history.reps,
        HISTORY_CONSTNATS.WEIGHT: history.weight,
        HISTORY_CONSTNATS.DATE: history.date
    }

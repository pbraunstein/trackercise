import hashlib

from app.constants import USERS, TAXONOMY, HISTORY, USERS_ID, USERS_EMAIL, USERS_NICKNAME, USERS_PASSWORD,\
    USERS_AUTHENTICATED, HISTORY_ID, HISTORY_USER_ID, HISTORY_EXERCISE_ID, HISTORY_SETS, HISTORY_REPS, HISTORY_WEIGHT,\
    HISTORY_DATE, TAXONOMY_NAME, TAXONOMY_IS_BACK, TAXONOMY_IS_CHEST, TAXONOMY_IS_SHOULDERS, TAXONOMY_IS_BICEPS,\
    TAXONOMY_IS_TRICEPS, TAXONOMY_IS_LEGS, TAXONOMY_IS_CORE, TAXONOMY_IS_BALANCE, TAXONOMY_IS_CARDIO,\
    TAXONOMY_IS_WEIGHT_PER_HAND


def hash_password(password):
    return hashlib.sha256(password).hexdigest()


def prepare_history_entry(entry):
    """
    Stringifies date of RepExercisesHistory entry
    """
    entry.date = str(entry.date)
    return entry


def all_data_to_dict(all_data):
    all_data[USERS] = list_user_objs_to_list_dicts(all_data[USERS])
    all_data[TAXONOMY] = list_taxonomy_objs_to_dicts(all_data[TAXONOMY])
    all_data[HISTORY] = list_history_objs_to_dicts(all_data[HISTORY])
    return all_data


def list_user_objs_to_list_dicts(user_list):
    return [_user_obj_to_dict(x) for x in user_list]


def list_taxonomy_objs_to_dicts(taxonomy_list):
    return [taxonomy_obj_to_dict(x) for x in taxonomy_list]


def list_history_objs_to_dicts(history_list):
    return [history_obj_to_dict(x) for x in history_list]


def _user_obj_to_dict(user):
    return {
        USERS_ID: user.id,
        USERS_EMAIL: user.email,
        USERS_NICKNAME: user.nickname,
        USERS_PASSWORD: user.password,
        USERS_AUTHENTICATED: user.authenticated
    }


def taxonomy_obj_to_dict(taxonomy):
    return {
        TAXONOMY_NAME: taxonomy.name,
        TAXONOMY_IS_BACK: taxonomy.is_back,
        TAXONOMY_IS_CHEST: taxonomy.is_chest,
        TAXONOMY_IS_SHOULDERS: taxonomy.is_shoulders,
        TAXONOMY_IS_BICEPS: taxonomy.is_biceps,
        TAXONOMY_IS_TRICEPS: taxonomy.is_triceps,
        TAXONOMY_IS_LEGS: taxonomy.is_legs,
        TAXONOMY_IS_CORE: taxonomy.is_core,
        TAXONOMY_IS_BALANCE: taxonomy.is_balance,
        TAXONOMY_IS_CARDIO: taxonomy.is_cardio
    }


def history_obj_to_dict(history):
    return {
        HISTORY_ID: history.id,
        HISTORY_USER_ID: history.user_id,
        HISTORY_EXERCISE_ID: history.exercise_id,
        HISTORY_SETS: history.sets,
        HISTORY_REPS: history.reps,
        HISTORY_WEIGHT: history.weight,
        HISTORY_DATE: history.date
    }

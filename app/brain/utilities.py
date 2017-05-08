import hashlib

from app.constants import USERS, TAXONOMY, HISTORY


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
    return "plop"


def taxonomy_obj_to_dict(taxonomy):
    return "plop"


def history_obj_to_dict(history):
    return "plop"

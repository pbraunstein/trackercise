import hashlib


def hash_password(password):
    return hashlib.sha256(password).hexdigest()


def prepare_history_entry(entry):
    """
    Stringifies date of RepExercisesHistory entry
    """
    entry.date = str(entry.date)
    return entry


def serialize_all_data(all_data):
    pass


def serialize_taxonomy_list(taxonomy_list):
    pass


def serialize_history_list(history_list):
    pass


def _serialize_taxonomy(taxonomy):
    pass


def _serialize_hisory(history):
    pass
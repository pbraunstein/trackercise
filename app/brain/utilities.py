import hashlib


def hash_password(password):
    return hashlib.sha256(password).hexdigest()


def prepare_history_entry(entry):
    """
    Stringifies date of RepExercisesHistory entry
    """
    entry.date = str(entry.date)
    return entry

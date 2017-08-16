# Classes used to group constants
class USERS_CONSTANTS:
    GROUP_NAME = 'users'
    ID = 'users_id'
    EMAIL = 'users_email'
    NICKNAME = 'users_nickname'
    PASSWORD = 'users_password'
    AUTHENTICATED = 'users_authenticated'


class TAXONOMY_CONSTANTS:
    GROUP_NAME = 'taxonomy'
    ID = 'taxonomy_id'
    NAME = 'taxonomy_name'
    IS_BACK = 'taxonomy_is_back'
    IS_CHEST = 'taxonomy_is_chest'
    IS_SHOULDERS = 'taxonomy_is_shoulders'
    IS_BICEPS = 'taxonomy_is_biceps'
    IS_TRICEPS = 'taxonomy_is_triceps'
    IS_LEGS = 'taxonomy_is_legs'
    IS_CORE = 'taxonomy_is_core'
    IS_BALANCE = 'taxonomy_is_balance'
    IS_CARDIO = 'taxonomy_is_cardio'
    IS_WEIGHT_PER_HAND = 'taxonomy_is_weight_per_hand'


class HISTORY_CONSTANTS:
    GROUP_NAME = 'history'
    ID = 'history_id'
    USER_ID = 'history_user_id'
    EXERCISE_ID = 'history_exercise_id'
    SETS = 'history_sets'
    REPS = 'history_reps'
    WEIGHT = 'history_weight'
    DATE = 'history_date'
    DISTANCE = 'history_distance'
    DURATION = 'history_duration'


class FILE_HANDLES:
    USERS = 'users'
    REP_TAXONOMY = 'rep_taxomony'
    REP_HISTORY = 'rep_history'
    TIME_TAXONOMY = 'time_taxonomy'
    TIME_HISTORY = 'time_history'
    SEPARATOR = '_'
    EXTENSION = '.csv'

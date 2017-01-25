class LoginResults(object):
    """
    Enum class so everyone can agree on a common language for logging in
    """
    LOGGED_IN = 0
    NO_SUCH_USER = 1
    INCORRECT_PASSWORD = 2
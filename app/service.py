from app import db
from app.models import Users, RepExercisesTaxonomy, RepExercisesHistory


class UsersService(object):
    """
    Service class for interacting with the Users SQLAlchemy object

    I N T E R F A C E   G U A R A N T E E D
    ---------------------------------------
    get_user_with_email(email):
        -- Returns the Users with the email passed in. Returns None if no user exists with the given email

    add_user_to_database(email, nickname, hashed_password):
        -- Adds a user to the database

    user_with_email_already_exists(email):
        -- Returns True if a user with that email already exists. Otherwise returns False.

    get_list_of_all_users():
        -- Exports all Users as a list [Users(), ...]
    """
    @staticmethod
    def get_user_with_email(email):
        return db.session.query(Users).filter(Users.email == email).first()

    @staticmethod
    def add_user_to_database(email, nickname, hashed_password):
        new_user = Users(email=email, nickname=nickname, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

    @staticmethod
    def user_with_email_already_exists(email):
        users = Users.query.all()
        user_emails = [x.email for x in users]
        if email in user_emails:
            return True
        else:
            return False

    @staticmethod
    def get_list_of_all_users():
        return list(Users.query.all())


class RepExercisesTaxonomyService(object):
    """
    Service class for interacting with the RepExercisesTaxonomy SQLAlchemy object

    I N T E R F A C E   G U A R A N T E E D
    ---------------------------------------
    get_list_of_all_exercises():
        -- Exports all RepExercisesTaxonomy entries as a list [RepExercisesTaxonomy(), ...]

    get_list_of_taxonomies_by_exercise_ids():
        -- Exports all RepExercisesTaxonomy entries corresponding to a given list of exercise_ids
            [RepExercisesTaxonomy(), ...]

    add_entry_to_db(entry):
        -- Takes a RepExercisesTaxonomy and adds it to the database
    """
    @staticmethod
    def get_list_of_all_exercises():
        return list(RepExercisesTaxonomy.query.all())

    @staticmethod
    def get_list_of_taxonomies_by_exercise_ids(exercise_ids):
        return list(db.session.query(RepExercisesTaxonomy).filter(RepExercisesTaxonomy.id.in_(exercise_ids)))

    @staticmethod
    def add_entry_to_db(entry):
        db.session.add(entry)
        db.session.commit()


class RepExercisesHistoryService(object):
    """
    Service class for interacting with the RepExercisesHistory SQLAlchemy object

    I N T E R F A C E   G U A R A N T E E D
    ---------------------------------------
    get_list_of_all_history():
        -- Exports all RepExercisesHistory entries as a list [RepExercisesHistory(), ...]

    get_list_of_users_exercises(user_id):
        -- Exports all RepExercisesHistory entries of a particular user [RepExercisesHistory(), ...]

    get_user_history_by_exercise(user_id, exercise_id):
        -- Exports all RepExerciseHistory entries of a particular user and particular exercise
            [RepExercisesHistory(), ...]

    add_entry_to_db(entry):
        -- Takes a RepExercisesHistory and adds it to the database
    """
    @staticmethod
    def get_list_of_all_history():
        return list(RepExercisesHistory.query.all())

    @staticmethod
    def get_list_of_users_exercises(user_id):
        return list(db.session.query(RepExercisesHistory).filter_by(user_id=user_id).all())

    @staticmethod
    def get_user_history_by_exercise(user_id, exercise_id):
        return list(db.session.query(RepExercisesHistory).filter_by(user_id=user_id, exercise_id=exercise_id).all())

    @staticmethod
    def add_entry_to_db(entry):
        db.session.add(entry)
        db.session.commit()

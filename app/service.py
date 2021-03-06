from app import db
from app.models import Users, RepExercisesTaxonomy, RepExercisesHistory, TimeExercisesTaxonomy, TimeExercisesHistory


class UsersService(object):
    """
    Service class for interacting with the Users SQLAlchemy object and database

    I N T E R F A C E   G U A R A N T E E D
    ---------------------------------------
    get_user_with_email(email):
        -- Returns the Users with the email passed in. Returns None if no user exists with the given email

    mark_user_as_authenticated(user):
        -- Updates the authenticated column to True for the user passed in

    mark_user_as_not_authenticated(user):
        -- Updates the authenticated column to False for the user passed in

    add_user_to_database(new_user):
        -- Adds a user to the database. The argument passed in is of type Users.

    user_with_email_already_exists(email):
        -- Returns True if a user with that email already exists. Otherwise returns False.

    get_list_of_all_users():
        -- Exports all Users as a list [Users(), ...]
    """
    @staticmethod
    def get_user_with_email(email):
        return db.session.query(Users).filter(Users.email == email).first()

    @staticmethod
    def mark_user_as_authenticated(user):
        db.session.query(Users).filter(Users.id == user.id).update({Users.authenticated: True})
        db.session.commit()

    @staticmethod
    def mark_user_as_not_authenticated(user):
        db.session.query(Users).filter(Users.id == user.id).update({Users.authenticated: False})
        db.session.commit()

    @staticmethod
    def add_user_to_database(new_user):
        db.session.add(new_user)
        db.session.commit()

    @staticmethod
    def user_with_email_already_exists(email):
        users = Users.query.all()
        user_emails = [x.email.lower() for x in users]
        email = email.lower()
        if email in user_emails:
            return True
        else:
            return False

    @staticmethod
    def get_list_of_all_users():
        return list(Users.query.all())

    @staticmethod
    def change_password(user, new_password):
        db.session.query(Users).filter(Users.id == user.id).update({Users.password: new_password})
        db.session.commit()


class RepExercisesTaxonomyService(object):
    """
    Service class for interacting with the RepExercisesTaxonomy SQLAlchemy object and database

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
    Service class for interacting with the RepExercisesHistory SQLAlchemy object and database

    I N T E R F A C E   G U A R A N T E E D
    ---------------------------------------
    get_list_of_all_history():
        -- Exports all RepExercisesHistory entries as a list [RepExercisesHistory(), ...]

    get_list_of_users_exercises(user_id):
        -- Exports all RepExercisesHistory entries of a particular user [RepExercisesHistory(), ...]

    get_user_history_by_exercise(user_id, exercise_id):
        -- Exports all RepExerciseHistory entries of a particular user and particular exercise
            [RepExercisesHistory(), ...]
        -- Entries are returned in ascending order by date (i.e. earlier to later)

    get_user_history_by_date(user_id, exercise_date):
        -- Exports all RepExerciseHistory entries of a particular user performed on a particular date
            [RepExercisesHistory(), ...]
        -- Does not make any guarantees regarding the order of elements returned

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
    def get_user_history_by_date(user_id, exercise_date):
        return list(db.session.query(RepExercisesHistory).filter_by(user_id=user_id, date=exercise_date).all())

    @staticmethod
    def add_entry_to_db(entry):
        db.session.add(entry)
        db.session.commit()


class TimeExercisesTaxonomyService(object):
    """
    Service class for interacting with TimeExercisesTaxonomy SQLAlchemy object and database

    I N T E R F A C E   G U A R A N T E E D
    ---------------------------------------
    get_list_of_all_exercises():
        -- Exports all TimeExercisesTaxonomy entries as a list [TimeExercisesTaxonomy(), ...]

    add_entry_to_db(entry):
        -- Adds a TimeExercisesTaxonomy to the database
    """
    @staticmethod
    def get_list_of_all_exercises():
        return list(TimeExercisesTaxonomy.query.all())

    @staticmethod
    def add_entry_to_db(entry):
        db.session.add(entry)
        db.session.commit()


class TimeExercisesHistoryService(object):
    """
    Service class for interacting with the TimeExercisesHistory SQLAlchemy object and database

    I N T E R F A C E   G U A R A N T E E D
    ---------------------------------------
    get_list_of_all_history():
        -- Exports all TimeExercisesHistory entries as a list [TimeExercisesHistory(), ...]

    get_list_of_users_exercises(user_id):
        -- Exports all TimeExercisesHistory entries of a particular user [TimeExercisesHistory(), ...]

    get_user_history_by_exercise(user_id, exercise_id):
        -- Exports all TimeExercisesHistory entries of a particular user and particular exercise
            [TimeExercisesHistory(), ...]
        -- Entries are returned in ascending order by date (i.e. earlier to later)

    get_user_history_by_date(user_id, exercise_date):
        -- Exports all TimeExercisesHistory entries of a particular user performed on a particular date
            [TimeExercisesHistory(), ...]
        -- Does not make any guarantees regarding the order of elements returned

    add_entry_to_db(entry):
        -- Takes a RepExercisesHistory and adds it to the database
    """
    @staticmethod
    def get_list_of_all_history():
        return list(TimeExercisesHistory.query.all())

    @staticmethod
    def get_list_of_users_exercises(user_id):
        return list(db.session.query(TimeExercisesHistory).filter_by(user_id=user_id).all())

    @staticmethod
    def get_user_history_by_exercise(user_id, exercise_id):
        return list(db.session.query(TimeExercisesHistory).filter_by(user_id=user_id, exercise_id=exercise_id).all())

    @staticmethod
    def get_user_history_by_date(user_id, exercise_date):
        return list(db.session.query(TimeExercisesHistory).filter_by(user_id=user_id,
                                                                     exercise_date=exercise_date).all())

    @staticmethod
    def add_entry_to_db(entry):
        db.session.add(entry)
        db.session.commit()

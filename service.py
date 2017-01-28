from app import db
from models import Users, RepExercisesTaxonomy, RepExercisesHistory


class UsersService(object):
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
    @staticmethod
    def get_list_of_all_exercises():
        return list(RepExercisesTaxonomy.query.all())


class RepExercisesHistoryService(object):
    @staticmethod
    def get_list_of_all_history():
        return list(RepExercisesHistory.query.all())

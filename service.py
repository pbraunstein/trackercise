from app import db
from models import Users


class UsersService(object):
    @staticmethod
    def get_user_with_email(email):
        return db.session.query(Users).filter(Users.email == email).first()

    @staticmethod
    def add_user_to_database(email, nickname, hashed_password):
        new_user = Users(email=email, nickname=nickname, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
